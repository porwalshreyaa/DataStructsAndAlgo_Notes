# GIT BASICS

#### Key Concepts

- Repository
- Clone
- Stage
- Commit
- Branch
- Merge
- Pull
- Push


### When we ```git init```:

Git creates a .git folder in our repo to tracks our changes in it.

#### Braches:

Main/Master

#### Staging

- Stage a file
```
git add <file>
```
- Stage all changes (modified and deleted etc all together)
```
git add --all
```
```
git add -A
```
- check stages files
```
git status
```
- unstage a file
```
git restore --staged <file>
```

#### Commit

- normal Commit
```
git commit -m "message"
```
- direct Commit (without staging, all tracked changes) 
```
git commit -a -m "message"
```
untracked changes won't be included
- for multiline commit don't add -m "message"
```
git commit
```
it'll open editor

##### These also exist...

- Create an empty commit
```
git commit --allow-empty -m "Start project"
```
- Use previous commit message (no editor):
```
git commit --no-edit
```
- Quickly add staged changes to last commit, keep message:
```
git commit --amend --no-edit
```

- See commit history
```
git log
```
- in short
```
git log --oneline
```
- which files changed
```
git log -stat
```

## Something New

### Tagging

#### A tag is like a label, to mark imp commits in work history like - "Releases", "Milestones", "Deployment" and "Hotfixes"

```
git tag <tagname>
```

