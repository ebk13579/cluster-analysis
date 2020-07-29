#!/usr/bin/python
#
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from test.utils import TestbedTestCase
import json
import main


VALID_PNG_IMAGE_DATA = '''data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAZAAAADMCAIAAADS5mKjAAAAGXRFWHRTb2Z0d2FyZQBBZG9
iZSBJbWFnZVJlYWR5ccllPAAAAyhpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek
5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuNi1jMTQwIDc5LjE2MDQ1M
SwgMjAxNy8wNS8wNi0wMTowODoyMSAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50
YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXB
NTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdX
JjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENDIDIwMTggKE1hY2ludG9zaCkiIHhtcE1NOkluc3RhbmNlSUQ9InhtcC5paWQ6N
zM4MUM4RUY1NTIwMTFFODlGQUVCQTY4MkI0NkFFMjQiIHhtcE1NOkRvY3VtZW50SUQ9InhtcC5kaWQ6NzM4MUM4RjA1NTIwMTFFODlGQUVCQTY4MkI0NkFF
MjQiPiA8eG1wTU06RGVyaXZlZEZyb20gc3RSZWY6aW5zdGFuY2VJRD0ieG1wLmlpZDo3MzgxQzhFRDU1MjAxMUU4OUZBRUJBNjgyQjQ2QUUyNCIgc3RSZWY
6ZG9jdW1lbnRJRD0ieG1wLmRpZDo3MzgxQzhFRTU1MjAxMUU4OUZBRUJBNjgyQjQ2QUUyNCIvPiA8L3JkZjpEZXNjcmlwdGlvbj4gPC9yZGY6UkRGPiA8L3
g6eG1wbWV0YT4gPD94cGFja2V0IGVuZD0iciI/Ph77jDMAABezSURBVHja7N17VE1Z4Afwub2VQiqVpCISJYlKKIznT2SMCYtBwpIhj2XGZJoxzGDQGIvlm
dfyNoMwnoUSlbrSS6WnpK7opffbb//yW41Jkx5nn3vOud/PH3fdzJp979l7n+/de999zxG9e/fuMwAAPpBDFQAAXyigCqAZtbW1RUVFb9++zc3NLSgoKCkp
KS4uLi0tJY/keXl5eUVFBXksKyurrKysqqqqqakhj9XV1eR/VKqnWI88UVVV7dChg4qKCnkkzzU0NNTU1NTV1cnzzp07a2lpkcf3f6LaAYEFzSEZlJGRkZm
Z+erVK4lEklWPPCF/kickgNh5Gzo6Orq6unp6et27d9fX1yeP3bp1I0969uxJ/h3NBCKsYckgkkTp6elJSUmJiYnkSXJyclxcHGup1DaGhob9+vUzMTHp3b
u3mZkZeUJSjAzW0JoILBAUMn1LSUmJj49/+vRpbGwsyabnz58L4LjI/NHc3NzCwqJ///7kSZ8+fXr06CEvL48WR2ABn5SVlZGhU3R0dGRkpFgsJo9VVVWyc
OAGBgbW1tY2NjZWVlYkyMgQTCQSoT8gsIBb6urqUlNT3ydUeHj4w4cPKyoqUC3GxsZ2dnYN+aWtrY06QWCB1CQkJJBsCgwMvHPnzqtXr1AhzSOxNXr06BEj
RpAUwxI+AgvYkJSUFBISEhwcfPv27ZcvX6JC2obMHMeMGTN8+HASXjo6OqgQBBYwJicnhyRUQEDArVu3hLFezimDBw8eN24cyS8SXmpqaqgQBBa0RWxs7OX
Ll69duxYWFobaYIGiouLYsWP/p17Pnj1RIQgs+LTHjx+TnDp9+nRqaipqQ1psbW1dXV1JcvXp0we1gcCCfyGtQIZRfn5+Z86cyczMRIVwh4WFBUkuZ2dnS0
tL1AYCS6bV1NQ8ePDg0qVLJKfevHmDCuEyIyOj2bNnT506dejQoagNBJZsCQ4OPl2vqKgItcEvurq6M2fOnDVrFpILgSVw6enpJKT279+PHQkCYGJisnjxY
pJchoaGqA0ElnCUlJT4+fkdPHiQDKxQG8IzatQod3f3KVOmdOzYEbWBwOKxhw8fHjp06MSJE3V1dagNYZOTk/v6668XLlw4fPhw1AYCi08KCwtPnTq1c+dO
bE2QQUZGRitWrJgzZw5+vci8d8CoqKioefPmoV8BMXPmzEePHuGkYBACixk1NTUXL160tbXFWQqNDBgw4Pjx4xUVFThN2g9TwvbKy8vz9fXdtm1bfn4+agP
+i4qKysqVK5cuXYqvFDEllI6EhIT58+ejC0GrODs7h4SE4PTBlJA9MTExkydPxrkHbWZjY+Pv749TCYFFV2ho6JgxY3C+ASPMzc39/PxwWiGwmHfr1i2sqQ
MNenp6Bw8eLC8vx1mGwGLAhQsXjI2NcV4BVYqKilu3bi0rK8MZh8Bqo9u3b+NySMAmBQUFHx+fqqoqnH3Y1tAK9+/f9/T0jIqKQlU00NLS6tatW+fOnbW1t
bXqqaurd6inrKxMHpWUlOTl5d/fmF4kElXXq6lXUa+8HhlE5Ofnv3nzJjc3t6CggDxmZWXV1taihhuoqqr+/vvvixYtkpOTQ218CIHVGAkpElUksGTz8Eni
9KpnYmJiZGRkaGioo6PTtWtXklPkkZxIjL8iCTUSW4WFhe9TLDs7+3m9lJSU1NRU8p9ktit26dJl586d+OEEAqtp6enp33zzzfXr12XqqEk2WVlZmZmZ9ev
Xz9TUlPxJgokj762ysvLly5cvXrxIS0tLricWi8mfMtVABgYGe/fudXZ2xhmKwPp/xcXFXl5ee/bskYW5xrBhwwYNGmRubv4+nnh3h77MzMyEhIT4+HgyFo
6IiCBPZKGLWltbHzx4cPDgwQgsmQ4scvi7d+9euXKlUOtBJBINGTLEzs6O9HVLS8s+ffrQmNZJkUQiiYuLi4mJIeFFJvLkTwF3VxcXl127dsnyj3tkOrDI7
M/d3V14XVxZWXncuHEODg4kpMh0T0tLS0YatLa2NiUl5cmTJ2TmGBwcHB4eLsjDXL169c8//yybFwuU0cBKSkpasGBBSEiIkA5qxIgRY8eOHTlyJBlSCWwY
1TavX78myRUaGhoUFCSwa72SgfP+/fsXL16MwBK+9evXb968WRjHYm5uPnHiREdHx2HDhnFnsZyDcnNzSWb5+/tfvnw5OztbGAfVv3//s2fPDhgwQIYaUqZ
2nZFPWn19fb43maKi4vTp048dO/b8+XPsJGyturq66OhoHx8fMhQVxins6ekpOxfbkpXAIh+wM2bM4HW/1NLSWrZs2fXr10tKSpA7jJBIJKdOnZo1a5aKig
qv+4aqqurFixcRWAJx4MABMufnaV/U1dVdvXr1w4cPydAAEUMJGaEEBASQeub1F3COjo6CH3QLPLCSk5OtrKx4Op5as2ZNWFgY0oRlZMLo7e3N3+TavHkzA
ouX+LiyrqamtnTp0sDAwJqaGmSHdInF4nXr1vFuYy3Rt2/fJ0+eILB4Iz4+nndXWXBxcbly5Qp+ps81tbW15PNj4cKFioqK/OpRa9euRWDxwPbt23nUqyws
LPbv35+bm4to4LiysrLz58/z63qzRkZGsbGxCCyOkkgkdnZ2vOhJCgoKZOon1HG7sGVkZGzatIlHU8UtW7YgsDjn7NmzvOg9VlZWJ06cKC0txZnPa3V1df7
+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'''

VALID_JPG_IMAGE_DATA = '''data:image/jpeg;base64,/9j/4AAQSkZJRgABAAEBLAEsAAD/4QBEVGhpcyBpcyBhbiB1bmtub3duIEFQUCBtYXJrZX
IuIENvbXBsaWFudCBkZWNvZGVycyBtdXN0IGlnbm9yZSBpdC4K/+IARFRoaXMgaXMgYW4gdW5rbm93biBBUFAgbWFya2VyLiBDb21wbGlhbnQgZGVjb2Rlc
nMgbXVzdCBpZ25vcmUgaXQuCv/jAERUaGlzIGlzIGFuIHVua25vd24gQVBQIG1hcmtlci4gQ29tcGxpYW50IGRlY29kZXJzIG11c3QgaWdub3JlIGl0Lgr/
5ABEVGhpcyBpcyBhbiB1bmtub3duIEFQUCBtYXJrZXIuIENvbXBsaWFudCBkZWNvZGVycyBtdXN0IGlnbm9yZSBpdC4K/+UARFRoaXMgaXMgYW4gdW5rbm9
3biBBUFAgbWFya2VyLiBDb21wbGlhbnQgZGVjb2RlcnMgbXVzdCBpZ25vcmUgaXQuCv/mAERUaGlzIGlzIGFuIHVua25vd24gQVBQIG1hcmtlci4gQ29tcG
xpYW50IGRlY29kZXJzIG11c3QgaWdub3JlIGl0Lgr/5wBEVGhpcyBpcyBhbiB1bmtub3duIEFQUCBtYXJrZXIuIENvbXBsaWFudCBkZWNvZGVycyBtdXN0I
Glnbm9yZSBpdC4K/+gARFRoaXMgaXMgYW4gdW5rbm93biBBUFAgbWFya2VyLiBDb21wbGlhbnQgZGVjb2RlcnMgbXVzdCBpZ25vcmUgaXQuCv/pAERUaGlz
IGlzIGFuIHVua25vd24gQVBQIG1hcmtlci4gQ29tcGxpYW50IGRlY29kZXJzIG11c3QgaWdub3JlIGl0Lgr/6gBEVGhpcyBpcyBhbiB1bmtub3duIEFQUCB
tYXJrZXIuIENvbXBsaWFudCBkZWNvZGVycyBtdXN0IGlnbm9yZSBpdC4K/+sARFRoaXMgaXMgYW4gdW5rbm93biBBUFAgbWFya2VyLiBDb21wbGlhbnQgZG
Vjb2RlcnMgbXVzdCBpZ25vcmUgaXQuCv/sAERUaGlzIGlzIGFuIHVua25vd24gQVBQIG1hcmtlci4gQ29tcGxpYW50IGRlY29kZXJzIG11c3QgaWdub3JlI
Gl0Lgr/7QBEVGhpcyBpcyBhbiB1bmtub3duIEFQUCBtYXJrZXIuIENvbXBsaWFudCBkZWNvZGVycyBtdXN0IGlnbm9yZSBpdC4K/+4ARFRoaXMgaXMgYW4g
dW5rbm93biBBUFAgbWFya2VyLiBDb21wbGlhbnQgZGVjb2RlcnMgbXVzdCBpZ25vcmUgaXQuCv/vAERUaGlzIGlzIGFuIHVua25vd24gQVBQIG1hcmtlci4
gQ29tcGxpYW50IGRlY29kZXJzIG11c3QgaWdub3JlIGl0Lgr/wAARCAEAAQADABEAAREBAhEC/9sAQwAIBgYHBgUIBwcHCQkICgwUDQwLCwwZEhMPFB0aHx
4dGhwcICQuJyAiLCMcHCg3KSwwMTQ0NB8nOT04MjwuMzQy/9sAQwEJCQkMCwwYDQ0YMiEcITIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyM
jIyMjIyMjIyMjIyMjIy/9sAQwIJCQkMCwwYDQ0YMiEcITIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIy/8QBogAA
AQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoLEAACAQMDAgQDBQUEBAAAAX0BAgMABBEFEiExQQYTUWEHInEUMoGRoQgjQrHBFVLR8CQzYnKCCQoWFxgZGiU
mJygpKjQ1Njc4OTpDREVGR0hJSlNUVVZXWFlaY2RlZmdoaWpzdHV2d3h5eoOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0t
PU1dbX2Nna4eLj5OXm5+jp6vHy8/T19vf4+foBAAMBAQEBAQEBAQEAAAAAAAABAgMEBQYHCAkKCxEAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhc
RMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaX
mJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMAAAERAhEAPwDwPZX4afiEQ2UG8Q2UHRENlBv
ENlBvENlBvENlBvENlBvENlBvENlBvENlBvENlB0RDZQbxDZQbxDZQbxDZQbxDZQbRDZQbxDZQbxDZQdEQ2UG8Q2UG8Q2UG8Q2UG8Q2UG8Q2UG8Q2UG8Q2U
G8Q2UHRENlBvENlBvENlBvEsbKD+I4hsoN4hsoOiIbKDeIbKDeIbKDeIbKDeIbKDeIbKDeIbKDeIbKDeIbKDoiGyg3iGyg3iGyg3iGyg3iGyg2iGyg3iGyg
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'''


class MainTests(TestbedTestCase):
    def setUp(self):
        super(MainTests, self).setUp()
        self.app = main.app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_request_to_unknown_url(self):
        response = self.client.get('/unknown')
        self.assertEqual('404 NOT FOUND', response.status)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(404, data.get('code'))
        # We don't really care what the message says,
        # as long as it was a 404 status

    def test_clusteranalysis_request_with_incorrect_http_method(self):
        response = self.client.get('/clusteranalysis')
        self.assertEqual('405 METHOD NOT ALLOWED', response.status)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(405, data.get('code'))
        # We don't really care what the message says,
        # as long as it was a 405 status


    def test_clusteranalysis_request_with_missing_json_header(self):
        response = self.client.post('/clusteranalysis',
                                    data=dict())
        self.assertEqual('400 BAD REQUEST', response.status)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(400, data.get('code'))
        self.assertEqual('The request content type must be application/json',
                            data.get('message'))

    def test_clusteranalysis_request_with_empty_payload(self):
        response = self.client.post('/clusteranalysis',
                                    json={})
        self.assertEqual('400 BAD REQUEST', response.status)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(400, data.get('code'))
        self.assertEqual('The request is missing the image parameter',
                            data.get('message'))

    def test_clusteranalysis_request_with_invalid_image_data(self):
        response = self.client.post('/clusteranalysis',
                                    json={'image': 'invaliddata'})
        self.assertEqual('400 BAD REQUEST', response.status)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(400, data.get('code'))
        self.assertTrue(
            data.get('message').startswith('Unable to process image data:'))

    def test_clusteranalysis_request_with_non_png_image_data(self):
        response = self.client.post('/clusteranalysis',
                                    json={'image': VALID_JPG_IMAGE_DATA})
        self.assertEqual('400 BAD REQUEST', response.status)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(400, data.get('code'))
        self.assertEqual('Only png images are accepted', data.get('message'))

    def test_clusteranalysis_request_with_invalid_directions(self):
        response = self.client.post('/clusteranalysis',
                                    json={
                                        'image': VALID_PNG_IMAGE_DATA,
                                        'direction': 'invalid'
                                    })
        self.assertEqual('400 BAD REQUEST', response.status)
        data = json.loads(response.data)
        self.assertFalse(data.get('success'))
        self.assertEqual(400, data.get('code'))
        self.assertEqual("Invalid read order 'invalid'", data.get('message'))

    def test_valid_clusteranalysis_requests(self):
        response = self.client.post('/clusteranalysis',
                                    json={'image': VALID_PNG_IMAGE_DATA})
        data = json.loads(response.data)
        self.assertEqual('200 OK', response.status)
        data = json.loads(response.data)
        self.assertTrue(data.get('success'))
        self.assertEqual(200, data.get('code'))
        self.assertIsInstance(data.get('result'), dict)
        self.assertIn('direction', data.get('result'))
        self.assertEqual('rtl', data.get('result').get('direction'))
        self.assertIn('clusters', data.get('result'))
        self.assertIsInstance(data.get('result').get('clusters'), list)
        for cluster in data.get('result').get('clusters'):
            self.assertIsInstance(cluster, dict)
            self.assertIn('bounds', cluster)
            self.assertIsInstance(cluster.get('bounds'), dict)
            self.assertIn('x', cluster.get('bounds'))
            self.assertIn('y', cluster.get('bounds'))
            self.assertIn('height', cluster.get('bounds'))
            self.assertIn('width', cluster.get('bounds'))


    def test_warmup_request_responds_200(self):
        """
        Asserts that a reuqest to /_ah/warmup is handled.
        """
        response = self.client.get('/_ah/warmup')
        self.assertEqual('200 OK', response.status)
