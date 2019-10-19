from consts import NP_TOKEN, NP_TRACING_URL
from requests import post


# example for use
# np.tracking('20450168245454', "0950830810")
class NP:
    def tracking(self, document_number, phone=""):
        data = self.__serialize_data(
            'TrackingDocument',
            'getStatusDocuments',
            self.__tracking_resources(document_number, phone))
        return self.__send_request(NP_TRACING_URL, data)

    def __serialize_answer(self, response):
        return {
            'delivery_cost': response['DocumentCost'],
            'weight': response['CheckWeight'],
            'recipient_name': response['RecipientFullName']
        }

    def __tracking_resources(self, document_number, phone):
        return {
            "methodProperties": {
                "Documents": [
                    {
                        "DocumentNumber": document_number,
                        "Phone": phone
                    }
                ]
            }
        }

    def __serialize_data(self, model_name, called_method, resources={}):
        return {
            'apiKey': NP_TOKEN,
            "modelName": model_name,
            "calledMethod": called_method,
            **resources
        }

    def __send_request(self, url, data):
        response = post(url, json=data).json()
        return self.__serialize_answer(
            response["data"][0]) if response["success"] is True else str(
            response["errors"])
