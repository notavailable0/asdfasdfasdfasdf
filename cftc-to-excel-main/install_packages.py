import sys
import subprocess
# implement pip as a subprocess:
modules = [
    "requests", 
    "XlsxWriter", 
    "beautifulsoup4", 
    "matplotlib", 
    "python-certifi-win32"
    ]

for m in modules:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', m])
    # process output with an API in the subprocess module:
    reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
    installed_packages = [r.decode().split('==')[0] for r in reqs.split()]
    print(installed_packages)