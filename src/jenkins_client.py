import requests
class JenkinsClient:
    def __init__(self, base_url, user=None, token=None):
        self.base_url=base_url.rstrip('/')
        self.auth=(user,token) if user and token else None
    def jobs(self):
        url=f"{self.base_url}/api/json?tree=jobs[name,url,color,lastBuild[number,result,duration,timestamp]]"
        r=requests.get(url,auth=self.auth,timeout=15); r.raise_for_status(); return r.json().get("jobs",[])
