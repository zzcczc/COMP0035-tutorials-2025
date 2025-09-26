# 5. Running tests in GitHub Actions

**Continuous Integration (CI)** is a development practice where code changes are automatically built, tested, and
validated as soon as they're committed to a repository.

GitHub provides a way to configure and run tests on a given action, such as when a new commit is made to your repository.
Their tool is **GitHub Actions**.

How to use GitHub Actions is [documented on GitHub's site](https://docs.github.com/en/actions/writing-workflows).

Creating and editing a workflow was covered in [activity 4-03](../4_code_quality/4-03-github-actions.md)

## Activity: Create a GitHub Actions workflow

- Go to your repository on GitHub
- Go to the **Actions** tab
- If you already have a workflow, then look for the 'New workflow' button; otherwise go to next step
- Find the workflow named **'Python package'** or **Python application** (both have similar steps) and click on **'Configure'**
    - You will see a workflow `.yml` file generated on the screen. Edit this with the following changes:

        - In the section `name: Install dependencies` at the end of this section but before the `name: Lint with Flake
          8` add a line to install your code `pip install -e .` and make sure pytest-cov is installed
          ```yaml
          - name: Install dependencies
            run: |
              python -m pip install --upgrade pip
              pip install flake8 pytest pytest-cov
              if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
              pip install -e .
          ```
        - In the section `- name: Test with pytest`, edit the line that runs pytest to one that also runs coverage, e.g. `pytest tests/test_playing_cards.py --cov-branch --cov-report=term-missing --cov=activities.starter.playing_cards`
        - Find the **'commit changes...'** button which is likely to top right of the screen and press it. Change the
          message if you wish and then **'Commit changes'** again.

This workflow will now run every time you push a change to GitHub. This is useful as it runs all your tests so you can
see if new code you have written breaks any previously working functionality.

> By default, GitHub Actions sends an email when the flow fails which you might find annoying!. You
can [change the notification settings](https://docs.github.com/en/account-and-profile/managing-subscriptions-and-notifications-on-github/setting-up-notifications/configuring-notifications#)
in GitHub.

## View the workflow results

To view the results of the workflow:

1. Go to the Action tab in your GitHub repository.
2. There should now be at least one workflow run. If all went well it has a green tick, if there were issues there will
   be a red cross. If there is a Amber/Yellow circle then the workflow is still running.
3. Click on the tick/cross/circle on the workflow.
4. Click on the tick/cross/circle on 'build'.
5. You should now see headings that correspond to the `name: ` sections in the .yml file.
6. Expand the `Test with pytest` section. The output should look similar to what you saw when you ran pytest from the
   terminal.

If there is a red cross then find the section at step 5 that has the red cross, expand it and see what the error message
it. It should say what failed and why. You will then need to fix the error.

Note: if the tests fail with a 'module not found' error this is likely due to either not adding the line
`pip install -e .` in the installation section of the .yml, or an issue with the content of pyproject.toml.

[Next activity](9-04-coverage.md)