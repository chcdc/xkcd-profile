# xkcd webcomics



📚 Update your README.md profile with a xkcd webcomics.

## SETUP
* A README.md file.
* Add a ```<!-- xkcd -->``` tag in your README.md file, with three blank lines below it.
The webcomic will be placed here.


## Instructions


To use this release, add a ```xkcd.yml``` workflow file to the ```.github/workflows``` folder in your repository with the following code:

```diff
name: xkcd-webcomics

on:
  schedule:
    - cron: '1 1 * * *'
  workflow_dispatch:

jobs:
  xkcd:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: xkcd-to-markdown
        uses: chcdc/xkcd-profile@v0.1
        with:
#         README_PATH: ./README.md # Optional. Defaults is ./README.md.
      - name: commit changes
        continue-on-error: true
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "GitHub Action"
          git add -A
          git commit -m "Updated xkcd commic daily" -a
      - name: push changes
        continue-on-error: true
        uses: ad-m/github-push-action@v0.6.0
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}\
          branch: main
