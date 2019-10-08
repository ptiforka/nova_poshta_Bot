from consts import NP_TOKEN, NP_TRACING_URL
from requests import post


# example for use
# np.tracking('20450168245454', "0950830810")
class NP:
    def tracking(self, document_number, phone=""):
        data = self.serialize_data(
            'TrackingDocument',
            'getStatusDocuments',
            self.tracking_resources(document_number, phone))
        return self.send_request(NP_TRACING_URL, data).json()

    def tracking_resources(self, document_number, phone):
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

    def serialize_data(self, model_name, called_method, resources={}):
        return {
            'apiKey': NP_TOKEN,
            "modelName": model_name,
            "calledMethod": called_method,
            **resources
        }

    def send_request(self, url, data):
        return post(url, json=data)
