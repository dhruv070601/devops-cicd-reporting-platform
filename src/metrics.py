from collections import Counter
def build_metrics(jobs):
    results=[j.get("lastBuild") for j in jobs if j.get("lastBuild")]
    states=Counter(x.get("result") or "RUNNING" for x in results)
    total=len(results)
    success=states.get("SUCCESS",0)
    return {"total_runs":total,"success":success,"failure":states.get("FAILURE",0),
            "success_rate":round(success*100/total,2) if total else 0,
            "jobs":len(jobs),"states":dict(states)}
