Wrapper for TOR requests. This is a simple wrapper for making requests through TOR like you would have done with 
the requests library. It is a simple wrapper around the requests library. It is useful for making requests through TOR without having to worry about the details of setting up TOR.

Example usage:
```python
import tor_requests as requests

response = requests.get('http://httpbin.org/ip')
```


Make sure that TOR is installed and running on your machine. If not, you can download it from [here](https://www.torproject.org/download/). TOR should be running when you execute tor_requests

Installation: 
```bash
pip install -r requirements.txt
```
