# Submodules

## Extract directory and its version history from a repository.

```bash
git clone <repository> only-directory

cd only-directory

# Create local branches for every remote branch (will shoot out some errors at the end, but it should work just fine)
for branch in `git branch -r | sed 's@origin/@ @'`;do `git branch $branch origin/$branch`;done

# Confirm that everything worked
git branch


# Remove the origin
git remote rm origin

# Extract history of directory and commit it (you should end up with a git repository of the directory's files and its commit history)
git filter-branch --subdirectory-filter <directory> -- --all
```

### Optional, you only need this if you want to rename branches to remove a prefix from their names.

```bash
# replace 'frontend/' with whatever prefix you need to remove.
for branch in `git br | grep frontend/ | sed 's@frontend/@ @'`;do `git br -m frontend/$branch $branch`;done
```

```bash
# Add origin for new repository and push it

git remote add origin <repository>

git push origin --all

# If you have tags
git push origin --tags
```

## Remove directory and its version history from a repository.

```bash
git clone <repository>

cd <repository>

# Create local branches for every remote branch (will shoot out some errors at the end, but it should work just fine)
for branch in `git branch -r | sed 's@origin/@ @'`;do `git branch $branch origin/$branch`;done

# Confirm that everything worked
git branch

# Remove directory and all its commit history from all branches
git filter-branch --force --index-filter 'git rm --cached --ignore-unmatch <directory> -r' --prune-empty --tag-name-filter cat -- --all

# force push (be careful and only do this if you 100% sure or you have a backup)
git push --all --force
```

## Add submodule

```bash
git submodule add <repository> <path>

# Example:
git submodule add ../hackathon-2021-frontend frontend

git add .

# Now commit and push
git commit -am "Accurate git commit message"

git push
```
