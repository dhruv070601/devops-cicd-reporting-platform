import argparse,json,os
from pathlib import Path
from jenkins_client import JenkinsClient
from metrics import build_metrics
from renderer import render
def main():
 p=argparse.ArgumentParser(); p.add_argument("--sample",action="store_true"); a=p.parse_args()
 if a.sample:
  jobs=[{"name":"build-api","lastBuild":{"number":42,"result":"SUCCESS","duration":120000,"timestamp":0}},
        {"name":"deploy-prod","lastBuild":{"number":18,"result":"FAILURE","duration":90000,"timestamp":0}}]
 else:
  jobs=JenkinsClient(os.environ["JENKINS_URL"],os.getenv("JENKINS_USER"),os.getenv("JENKINS_TOKEN")).jobs()
 metrics=build_metrics(jobs); Path("output").mkdir(exist_ok=True)
 Path("output/metrics.json").write_text(json.dumps(metrics,indent=2))
 Path("output/index.html").write_text(render(metrics))
 print(json.dumps(metrics,indent=2))
if __name__=="__main__": main()
