"""
import unittest

from unittest import mock

from fastapi.testclient import TestClient
class MyAPITestCase(unittest.TestCase):

  @mock.patch('genhealth_service.requests.post')
  def test_post_inference(client: TestClient, mock_post):

      rv = client.post('/predict', json={"history": [{"code": "64", "system": "age", "display": "64"},
                                                     {"code": "E11", "system": "ICD10CM",
                                                      "display": "Type 2 diabetes mellitus"},
                                                     {"code": "E11.3551", "system": "ICD10CM",
                                                      "display": "Type 2 diabetes mellitus with stable proliferative diabetic retinopathy, right eye"}],
                                         "num_predictions": 1, "generation_length": 10, "inference_threshold": 0.95,
                                         "inference_temperature": 0.95})

      mock_response = mock_post.return_value
      mock_response.return_value.ok = True
      mock_response.return_value = str({

          "predictions": [
              [
                  {
                      "system": "timegap",
                      "code": "00-01-month",
                      "display": "00-01-month"
                  },
                  {
                      "system": "ICD10CM",
                      "code": "E11",
                      "display": "Type 2 diabetes mellitus"
                  },
                  {
                      "system": "RXNORM-FREETEXT",
                      "code": "chlorthalidone",
                      "display": "chlorthalidone"
                  },
                  {
                      "system": "ICD10CM",
                      "code": "E11",
                      "display": "Type 2 diabetes mellitus"
                  },
                  {
                      "system": "RXNORM-FREETEXT",
                      "code": "levothyroxine",
                      "display": "levothyroxine"
                  },
                  {
                      "system": "ICD10CM",
                      "code": "E11.9",
                      "display": "Type 2 diabetes mellitus without complications"
                  }
              ]
          ],
          "history": [
              {
                  "code": "64",
                  "system": "age",
                  "display": "64"
              },
              {
                  "code": "E11",
                  "system": "ICD10CM",
                  "display": "Type 2 diabetes mellitus"
              },
              {
                  "code": "E11.3551",
                  "system": "ICD10CM",
                  "display": "Type 2 diabetes mellitus with stable proliferative diabetic retinopathy, right eye"
              }
          ]
      })
if __name__ == '__main__':
    unittest.main()
"""
#Ran out of time