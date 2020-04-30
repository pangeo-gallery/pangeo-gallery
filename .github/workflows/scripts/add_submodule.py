import os, json, subprocess, sys

if __name__ == '__main__':
    with open(os.environ['GITHUB_EVENT_PATH'], 'r') as f:
        ev = json.load(f)
    comment = ev['issue']['body']
    if comment.startswith('/add-submodule'):
        repo = comment.split('/add-submodule')[-1].strip()
        repo_url = f'https://github.com/{repo}.git'
        res = subprocess.run(
            f'git ls-remote {repo_url}', shell=True, stdout=subprocess.PIPE
        )
        if res.returncode == 128:
            print(f'{repo_url} does not appear to be a git repository')
            sys.exit(1)
        else:
            command = f'git checkout -b {repo} && git submodule add -b binderbot-built {repo_url} repos/{repo}'
            subprocess.check_call(command, shell=True, stdout=subprocess.PIPE)
            git_config_id = 'git config --global user.email "action@github.com" && git config --global user.name "GitHub Action"'
            git_commit = 'git add . && git commit -m "Setup repo"'
            git_push = f'git push -f --set-upstream origin {repo}'
            command = f"""{git_config_id} && {git_commit} && {git_push}"""
            subprocess.check_call(command, shell=True, stdout=subprocess.PIPE)
    else:
        sys.exit(1)
