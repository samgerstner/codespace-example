# Visual Studio Code and GitHub Codespaces example using Python and Flask

This is a sample Python and Flask application designed to show how easy it is to use Visual Studio Code and GitHub Codespaces.

The Python code is of the [Tower of Hanoi](https://en.wikipedia.org/wiki/Tower_of_Hanoi) puzzle that is often used to teach [recursion](https://en.wikipedia.org/wiki/Recursion) in computer science courses.

## What Is GitHub Codespaces

Your instant, ready to go, development box available anywhere, anytime, any device with Visual Studio Code in the browser or your machine with two extensions and nothing else.

The [presentation](presentation/GithubCodespaces.pdf) in the presentation folder gives a brief overview and if you have [five minutes to spare](https://youtu.be/ghLVQudQV4c) check out my video on it.

## See it in action

1. [Request access](https://github.com/features/codespaces/signup) to Codespaces for your github account.  Access should be given in a few hours.
1. After getting access to Codespaces; login to github and navigate to https://github.com/klabranche/pytoh.
1. Select `Use this template`. While you can create a Codespace right from `<> code`, `use this template` will create a copy of the repository in your profile. 

![use-this-template](https://user-images.githubusercontent.com/1045379/172484527-7c8f43d3-cb5f-4af7-9166-6508b844badc.png)

1. Fill out the form and select `Create repository from template`.
1. On your new repository select the `<> Code` menu; then `Codespaces` tab; then `Create codespace on main`.

![create-codespace-gui](https://user-images.githubusercontent.com/1045379/172485066-8b637491-547e-4c14-9de8-5954a401974b.png)

## Running the Python Examples

**Prerequisite:** Create your Codespace by following the [See it in action](#see-it-in-action) section.

### With Visual Studio Code In The Browser

The default action when creating or starting a Codespace from GitHub is to use the browser.

With your Codespace running:

1. In the terminal (CTRL+Shift+\`) type `python console.py` to run the command line version.
1. In the terminal type `flask run` and either click on the url in the text `* Running on http://127.0.0.1:5000 (Press CTRL+C to quit)` or select the `Open in Browser` in the popup message to run the web application version.
1. In the terminal press `CTRL+C` to stop the web application.
1. Close the tab that was running Visual Studio Code in the browser.

Now stop the Codespace:

1. Go back to your repository in GitHub; Select the `<> Code` menu; then `Codespaces` tab; then `Manage all`.
1. Select  `...` to the right of the Codespace; Select `Stop Codespace`.

We stopped the Codespace for two reasons:

1. To ensure we are only charged for what we use.  At this time, individual accounts aren't charged but it's still good practice to stop the Codespace when you are done.  By default, it will automatically turn off after 30 minutes of inactivity.
1. To ensure the port we opened for Flask is ready for our next example.

>:thumbsup: No installs, no setup and configuration.  It just ran.  That's what Codespaces with Visual Studio Code in the browser does for you.

### With Visual Studio Code On Your Machine
Visual Studio Code on your machine requires two extensions to work with GitHub Codespaces:

* [GitHub Codespaces](https://marketplace.visualstudio.com/items?itemName=GitHub.codespaces)
* [Remote Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

You will be prompted to install the extensions when opening a Codespace if they are not installed.

You will be prompted to login into GitHub if you have not already done so in Visual Studio Code.

1. In Visual Studio Code open the command palette by typing `CTRL+SHIFT+P`; Type `codespaces` and select `Connect to CodeSpaces`.  Select the Codespace from the drop down list.
   * Every Codespace created by GitHub is given a random name. Select the randomly named Codespace; 
   
![codespaces-commands](https://user-images.githubusercontent.com/1045379/172910290-2c360cc0-c0e4-44e3-b773-2dfc7766250b.png)

With your Codespace running:

1. Open the terminal (CTRL+Shift+\`); type `python console.py` to run the console sample.
1. In the terminal; type `flask run` and either click on the url in the text `* Running on http://127.0.0.1:5000 (Press CTRL+C to quit)` or select `Open in Browser` in the popup message to run the web application version.
   * If you get: 
      * Address already in use Port 5000 is in use by another program. Either identify and stop that program, or start the server with a different port. OR
      * 504 Gateway Timeout. The port forwarding timed out while trying to create a connection.
   * Stop the Codespace and restart it.  This is due to running the Flask example in another session for the same Codespace.
3. In the terminal; press `CTRL+C` to stop the web application.
4. To stop the Codespace session; click `Codespaces` in the lower left hand corner of Visual Studio Code.  Select `Stop current codespace` in the drop down menu opened by the command palette.
 
You can also use Visual Studio Code's command palette (`CTRL+Shift+P`) to manage your Codespaces.  To see all the available options type `codespaces` in the command palette window.
 
## Debugging

You can debug with the browser and desktop version of Visual Studio Code with Codespaces.

### Debugging console.py 

1. Select `console.py` file in the explorer (left hand icon menu).

![explorer-icon](https://user-images.githubusercontent.com/1045379/172488635-ccaf95c0-ab8c-42a9-bf12-b7beea7818f7.png)

2. Put a breakpoint on line 11 by clicking to the left of the line number.
1. Select Run and Debug (left hand icon menu).
1. Select `Python: Current File` in the drop down menu at the top right of the Run and Debug window.

![run-debug-icon](https://user-images.githubusercontent.com/1045379/172489692-01704127-e19e-4330-b407-f68ec36a3c14.png)

5. Press `F5` to start a debugging session.
1. At the prompt in the terminal enter something other than a number.
1. The breakpoint should now be hit.  Press `F5` to continue.

### Debugging app.py (Flask)

1. Select `app.py` in the explorer (left hand icon menu).
1. Put a breakpoint on line 9 by clicking to the left of the line number.
1. Select Run and Debug icon (left hand icon menu).
1. Select `Python: Flask` in the drop down menu at the top right of the Run and Debug window.
1. Press `F5` to start a debugging session.
1. Either click on the url in the text `* Running on http://127.0.0.1:5000 (Press CTRL+C to quit)` or select `Open in Browser` in the popup message to run the web application version of the Tower of Hanoi sample.
1. The web page should now be spinning without anything showing yet.  That's because the breakpoint has been hit before we have returned the home page.
1. In Visual Studio Code; press `F5` to continue and the home page should now load.
1. Press `Shift+F5` to end the debugging session.

## Sharing your app with others (Port Forwarding)

By default, ports used by the container are private to your session only.  However, you can make it public to show your work to others.  This is ideal for a simple demo.  

>:exclamation: Don't do this for anything other than a demo.  This is not meant for production work or replacement of a server or web hosting.

1. Select `PORTS` tab that is in the terminal window.
1. Right click port 5000; select `Port Visibility` and then `Public`.

![port-public](https://user-images.githubusercontent.com/1045379/172489409-50a28c26-15dc-4e3f-a71e-46116c48676a.png)


3. Select `TERMINAL` tab again and then type at the command prompt `flask run`.

Now when you open the browser you will have a new url.  You can share this URL with others.

How is this working?  The GitHub Codespace is in the cloud and has setup this link to the outside world with the container.  Remember, the connection is to the container in the cloud not your local computer.

Let's go ahead and undo that now.  It's great for a quick pinch demo but we don't recommend it for much more than that.  

1. Select `PORTS` tab that is in the terminal window.
1. Right click port 5000; select `Port Visibility` and then `Private`.

## Customize the container

The [default container](https://docs.github.com/en/codespaces/setting-up-your-project-for-codespaces/introduction-to-dev-containers#using-the-default-dev-container-configuration) from GitHub has an assortment of compilers, runtimes and tools on it.  For example, `console.py` would run immediately without any customization since Python is installed on the default container.

Flask, however is not.  In order for `app.py` to run without any extra manual steps we created the [devcontainer.json](https://github.com/klabranche/pytoh/blob/main/.devcontainer/devcontainer.json) file in the .devcontainer folder.

We added a post create command to run `pip` to install our `requirements.txt`.  Line 50 of the `devcontainer.json` reads:

`"postCreateCommand": "pip3 install --user -r requirements.txt",`

This installs Flask whenever a new container is created.

Creating this file in Visual Studio Code is a breeze by opening the command palette (`CTRL+Shift+P`) and typing `remote-container: Add Development Container Configuration Files` and follow the prompts.  

There is a lot more you can do with [customizing your container](https://code.visualstudio.com/docs/remote/create-dev-container).

## Cleanup

You can delete the Codespace in GitHub or in Visual Studio Code.

>:warning: Deleting a Codespace deletes all work that was being done in the container.  Be sure to `push` your changes up to GitHub before deleting a Codespace.

### Deleting Codespace using GitHub
1. Select the `<> Code` menu.
1. Select `manage all`.  
1. For each Codespace in the list of Codespaces you want to delete select `...` menu and then select `Delete`.

### Deleting Codespace using Visual Studio Code
1. Click `Codespaces` in the lower left hand corner of Visual Studio Code. 

![codespace-in-vs](https://user-images.githubusercontent.com/1045379/172491677-53f9a1a1-9763-4f57-9c61-4dfef7369da8.png)

2. Select `Stop Current Codespace` in the drop down menu opened by the command palette.
1. Click `Codespaces` again; Select `Delete Codespace` in the drop down menu opened by the command palette.
1. Select the codespace you want to delete from the drop down list.
1. Select `delete` when asked to confirm deletion.

## Learn More

There is so much more to learn about Visual Studio Code and GitHub Codespaces. To learn more check out [GitHub Codespaces docs](https://docs.github.com/en/codespaces).

[Learn more about Python](https://docs.microsoft.com/en-us/learn/modules/intro-to-python/)

[Learn more about Flask](https://flask.palletsprojects.com/en/2.1.x/quickstart/#a-minimal-application)

[Deploy a Flask app to Azure](https://docs.microsoft.com/en-us/azure/app-service/quickstart-python?toc=%2Fazure%2Fdeveloper%2Fpython%2Ftoc.json&bc=%2Fazure%2Fdeveloper%2Fbreadcrumb%2Ftoc.json&tabs=flask%2Cwindows%2Cazure-portal%2Cterminal-bash%2Cvscode-deploy%2Cdeploy-instructions-azportal%2Cdeploy-instructions-zip-azcli) 

See this [application running](https://tohsolved.azurewebsites.net/) in Azure's free [website as a service](https://docs.microsoft.com/en-us/azure/app-service/overview) tier.

Check out [Azure web app for containers](https://azure.microsoft.com/en-us/services/app-service/containers/) to learn more about deploying containerized web apps.

[Azure App Service Docs](https://docs.microsoft.com/en-us/azure/app-service/) is a great jumping off point to learn more about Azure App Services.
