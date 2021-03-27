git checkout book
git reset --hard origin/main
git log -3
python -m api.common.update_md
git config --local user.email 'action@github.com'
git config --local user.name 'github-actions'
git add --all
git commit --allow-empty -m 'Inject problems'
