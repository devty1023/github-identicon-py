from git_identicon import git_identicon

x = git_identicon.Git_Identicon("itsafreakingdemo",size=64)
x.image.save("test.png", "PNG")
