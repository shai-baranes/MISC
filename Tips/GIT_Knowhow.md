# GIT Knowhow:

Advanced topics: <https://www.youtube.com/watch?v=lG90LZotrpo>

Find animated cheatsheet from Alex at: <https://philomatics.com/git-cheatsheet-release>

## Basics

* **git init** to create local repository
* Create '.gitignore' file with folders and files to never stage
  - note that you can stage only specific files under ignored folders by exclusion: !file\_name
* **git add .** staging all files while ignoring the unwanted files, e.g. repository or virtual env
* **git stash** Stashes all tracked changes.
* **git stash -u | git stash --include-untracked** Stashes all tracked and untracked files.
* **git stash -S**  Stashes only the staged files.
* **git stash -k**  Stashes only the unstaged files, leaving the staged
* **git reset --hard**  discarding local changes - such as stashed
* **git clean -fd** rarely for cases you also want to clean the untracked/ new files. Irreversible!
* **git status** to track on the staged files, modified files and active/checked-out branch
* **git diff** gives you a quick diff snapshot, current pre-staged vs. last commit state
* **git diff - - staged** more popular, gives you a quick diff snapshot, current staged vs. last commit state
* **git reset** if having undesired files staged, update the '.gitignore' and run re-staging
* **git commit -m "first commit"**
* **git branch -M main** renames/Modify the current active to main
* **git branch** to see current active branch
* **git log** track on commits inwards below for more advance on this!
  + **git log [FILE\_NAME]** track the historical commits on a specific file
  + **git log -L ,:[FILE\_NAME]** track the historical commits on a specific file with git diff per commit – per entire file. Note that it is case-sensitive for file/folders names.
  + **git log -L ,15:25[FILE\_NAME]** track the historical commits on a specific file with git diff per commit – per selective file slice using lines numbering.
  + **git log -S [STRING] -p** tracking historical commits on a specific string on all files, with git diff per commit. Git grep may not find it if was removed from the code base at a certain point.
  + **git grep [STRING]** returns only the lines where the exact phrase, and not as subset, is found.
* **git remote add origin https://github.com/shai-baranes/Slot\_machine.git**
  get link from GitHub for the first commit only or for connecting new computer…
* **git push -u origin main** also for first commit
* **git push -u origin from\_perplexity** and if we wanted to update a certain branch out of many to be in focus in our local repo.
* *Note that git creates the first branch as 'master', yet we can decide to change it to 'main' and we shall have no history for 'master'.*
* *If all branches are stored locally, no need to pull from repository to get to an earlier branch/code.*

## Advance

* **git log --all --decorate --oneline --graph** \n
    To display a commit per line, 
   *also depicting visually the tree branches – can be in my Alias: >> git loog*
  ----------

\* **8f5a062** HEAD -> main, origin/main updating the README file

\* **2f4c8be** adding README.md

\* **faad10c** first commit
  ----------

* **git reflog** another way to see all with head [i] for timeline tracking – not replacing the above
* **gitk** another lovely way to get a visual representation of all commits and branches!
* **git branch side\_branch** ; **git branch for\_testing** adding 2 more branches
* **git branch** to see all branches
* **git checkout side\_branch** HEAD pointer is now moved to the new branch
* **git checkout -b side\_branch** for both creating and checking out into the new branch
* **git rebase -i HEAD~4** checkout back in time 4 commits – from where we are now; it is possible to replace HEAD w/ main or master – also enables to delete only partially.
* **git reset –hard HEAD@{5}** to undo the above rebase cmd, helpful to track rebase changes by running: **git reflog**; note that **git reset –hard HEAD@{1}** will now undo the undo 😊
* **git commit -a -m "commit info"** to both 'stage' and 'commit' any modified file
* **git commit --amend** append to existing commit before it is pushed
* **git commit --amend --no-edit** append to existing commit, prior to push, without changing the commit log message
* **git checkout [File\_Name]** before commit, you can undo your changes and restore the last commit revision of that file – note that CTR+Z can revert back your local non-committed changes
* **git checkout -p [File\_Name]** you can scan your changes top to bottom one by one and either approve or reject each of the recent local saved changes
* **To merge 2 diff branches , both stemmed from the master/main:**
  + **git checkout master** move pointer/header back to master
  + **git diff master..side\_branch** shows what will change when merge side to master
  + **git merge master\_branch**
    from the master we merge the side\_branch, ff merge since having direct path
  + **git branch --merged** shows which branches merged to the branch we're on
  + **git branch -d side\_branch**
     after the above cmd we can safely delete the 'side\_branch'
  + **git branch -D side\_branch** forcibly deleting unmerged branch. try to avoid.
  + **git push --all origin** to push all local branches to the remote git-hub repository
* **Working with a clone from remote git repo:**
  + **git clone** [**https://github.com/shai-baranes/MISC.git**](https://github.com/shai-baranes/MISC.git)*taken from 'Code' in repo*get you repo to other user or other folder of yours…
  + **git fetch origin** if during activity, you want to check whether a new change committed since.
  + **git status** now tells you how behind are you; e.g.
    *Your branch is behind 'origin/main' by 1 commit, and can be fast-forwarded. use "git pull" to update your local branch*
  + **git diff origin/main** quickly see changes. *if your main is 'master' then master it is*
  + **git pull** to pull these new changesno need to commit
* **To delete a cached file that is not ignored although listed since already in repository:**
  + **git rm -r --cached .** important if you accidently added unwanted files!
  + **git add .** you get something similar like the below output
* **what to do in case I am not satisfied on my last changes revert?**
  + **git reset --merge** if there are conflicts and I'd like to revert to previous state – instead of changing files, stage the change changes and commit resolution.
  + **git reset --hard HEAD** force action to discard all changes since last commit.
  + **git checkout main [or master]** to move to my main branch before killing the unwanted branch.
  + **git clean -n** safe step: If still have untracked files, this cmd will clean it – vs.
  + **git clean -f** permanent step: If still have untracked files, this cmd will clean it.
  + **git branch -d <branch-name>** if changes are merged or **git branch -D <branch-name>** if changes are not merged and I don't really care.
  + **git push origin --delete <branch-name>** to delete the undesired branch from the remote/github repository.
  + **git fetch -p** recommended after deleting the remote branch to avoid references to remote branch that is no longer exist.

## Aliases

For more info: <https://www.youtube.com/watch?v=CAnQ4b0uais>

* **git config --global alias.last "log -1 HEAD"** example for adding a basic alias for logging the last commit; execute by: >> **git last**
  ***\*note: in my case, the 'single quote' for the alias was not working!***
* **git config --global --edit** Another way to edit/add aliases
* **git config --get alias.[YOUR\_ALIAS]** for inspecting a specific alias, wheter exists and what aimed to do?
* **git config --get-regexp ^alias** listing your user defined aliases – entire list

## Worktree for more info: <https://www.youtube.com/watch?v=ntM7utSjeVU&t=17s>

* **git worktree list** gives the list of worktrees / cloned and some maybe altered directories.
  *the first in line is the default worktree – the origin.*
* **git worktree add .worktree\hotfix main** *[or master]*
  clone the current project to .worktree\hotfix folder – under current path '.' and get there with only the committed code! – main branch!

*now git worktree list displays 2 items.*

*Different branches are checked-out in diff worktrees can't check-out again*

* **git worktree remove .** remove the worktree in current location – *to be followed by folder deletion*

## Extras

***lovely tips from****: https://www.youtube.com/watch?v=aolI\_Rz0ZqY&t=437s*

* **git blame [file\_name]** line by lines overview on a file while adding description on the non-committed lines.
* **git blame -L 15,26 [file\_name]** same as above, with a slicing option for the lines we want to focus on -> reminds the functionality of '**git diff [file\_name]'**.md by with the option to widen the FOV.
* **git blame -w -C -C -C -L 15,26 [FILE\_NAME]** each line has the developer who wrote it and the one to blame as needed – for muti-users project. Also ignoring white spaces and allegedly function/code movement if not affecting the functionality.
* **git config --global rere.enabled true** if you rebase and resolve conflicts, it learns how you resolve and do same in future conflict
* **git maintenance start** adds periodically crone job with maintenance task on my repository. All will run faster going forward.
* **git diff HEAD~1..HEAD** comparing last commit with the previous commit; you can also get the hash from 'git log' and compare using the hash numbers.

Also get recommended aliases from & the full list at the end of the video:
<https://www.youtube.com/watch?v=CAnQ4b0uais>

*TBD how to add/append to existing commit saw it on a YT vid earlier*

## Shared Repository basics

| **Step flow** | **Command** | **Purpose** |
| --- | --- | --- |
| Stash local changes | **git stash** | Save and clear local modifications |
| Pull from remote | **git pull** | Fetch and merge remote changes |
| Pull from remote Alternative | **git pull --rebase** | [Optional] To rebase my changes prior to the remote updates |
| View my stashed changes | **git stash list** | [Optional] if want to see local stashed changes |
| Apply stashed changes | **git stash pop** | Restore your local modifications |
| Resolve conflicts | **manual** | Fix any merge conflicts if present |
| Stage & Commit | **BASICS** | As usual … |
| Push changes | **git push** | Upload your merged changes to the remote |
