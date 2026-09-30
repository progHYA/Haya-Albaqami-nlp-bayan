#!/usr/bin/env python3
"""Set the learner repository identity without changing scientific evidence."""
import argparse,json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser(description=__doc__); p.add_argument('--repository',required=True)
a=p.parse_args(); url=a.repository.strip().rstrip('/')
m=re.fullmatch(r'https://github\.com/([A-Za-z0-9_-]+)/([A-Za-z0-9_.-]+)',url)
if not m or m.group(1)=='YOUR_USERNAME': p.error('Use your actual GitHub owner/repository URL')
owner,name=m.groups(); sp=ROOT/'PROJECT_SUMMARY.json'; summary=json.loads(sp.read_text())
old_url=summary['repository_url']; old_slug=old_url.removeprefix('https://github.com/'); new_slug=owner+'/'+name
for path in [ROOT/'README.md',ROOT/'SUBMISSION.yml',ROOT/'STUDENT_PROFILE.md',ROOT/'PROGRESS.md',*sorted((ROOT/'notebooks').glob('*.ipynb'))]:
 text=path.read_text().replace(old_url,url).replace('github/'+old_slug+'/blob/','github/'+new_slug+'/blob/')
 if path.name=='STUDENT_PROFILE.md':
  text=re.sub(r'(- GitHub username:) .*',r'\1 '+owner,text)
  text=re.sub(r'(- Public repository:) .*',r'\1 '+url,text)
 if path.name=='PROGRESS.md':
  text=re.sub(r'(\*\*Student GitHub:\*\*) .*',r'\1 '+owner+'  ',text)
  text=re.sub(r'(\*\*Repository:\*\*) .*',r'\1 '+url+'  ',text)
 if path.name=='SUBMISSION.yml': text=re.sub(r'^student_github: .*$', 'student_github: '+owner,text,flags=re.M)
 path.write_text(text)
summary['student_github']=owner;summary['repository_url']=url
sp.write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
print('Configured learner repository:',url)
print('Scientific results and completion flags were not modified.')
