"""Remove generated authentication credentials before publishing course reports."""
import json
import re
import sys
from pathlib import Path

SENSITIVE=re.compile(r'password|access_token|refresh_token|authorization|cookie|secret',re.I)
QUOTED=re.compile(r'''(?i)(\b(?:password|access_token|refresh_token|secret_key)\b["']?\s*[:=]\s*)(["'])(.*?)\2''')
JWT=re.compile(r'\beyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\b')
HEADER=re.compile(r'''(?im)(\b(?:authorization|cookie|set-cookie):\s*)[^\r\n'"]+''')

def redact_text(value):
    value=QUOTED.sub(lambda m:m[1]+m[2]+'[REDACTED]'+m[2],value)
    return JWT.sub('[REDACTED]',HEADER.sub(lambda m:m[1]+'[REDACTED]',value))

def redact(value):
    if isinstance(value,dict):
        if 'name' in value and 'value' in value and SENSITIVE.search(str(value['name'])):
            value={**value,'value':'[REDACTED]'}
        return {key:'[REDACTED]' if SENSITIVE.fullmatch(key) else redact(item) for key,item in value.items()}
    if isinstance(value,list):return [redact(item) for item in value]
    if isinstance(value,str):return redact_text(value)
    return value

def main():
    root=Path(sys.argv[1])
    assert root.is_dir(),'Allure results directory is missing'
    count=0
    for path in root.rglob('*'):
        if not path.is_file():continue
        if path.suffix=='.json':
            value=json.loads(path.read_text(encoding='utf-8'))
            path.write_text(json.dumps(redact(value),ensure_ascii=False),encoding='utf-8');count+=1
        elif path.suffix in {'.txt','.log','.properties'}:
            value=path.read_text(encoding='utf-8')
            path.write_text(redact_text(value),encoding='utf-8');count+=1
    print(f'Redacted {count} report data files.')
if __name__=='__main__':main()
