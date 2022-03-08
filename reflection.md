# Tkinter
## Tkinter being weird on MacOS
When a new window is made, it is made slightly lower and to the right. This becomes noticable over time.
MacOS overides most button styling.

None of this happens on my home PC which uses XFCE as a display manager and I suspect that this would not happen on windows either.

## Tkinter Scaling
Only now outside of replit did I realise that 

```python
createWindow.tk.call('tk', 'scaling', 2.0)
```
 makes widgets half size and that I should enter a value below 1.0 to achive scaled up widgets. I must not have noticed this mistake in replit's smaller tkinter window space.

# Git and GitHub
This project has allowed me to become more familiar with Git and GitHub since I no longer have the ability to rely on replit's cloud sync. I have found it quite easy to use and understand through VSCodes source control panel. This is due in part to the fact that this is a solo project and I have done nothing other than push to the main branch. Creating new branches, fetching, and making pull requests seems easy enough but I've yet to have the need to try. 

While I have been careful to commit often, on Friday I learned the hard way. I forgot to commit at the end of class and lost ~~30 minutes of progress. Luckily I realised as soon as I came home and remembered more or less how I created the 2 missing funcitons which made their recreation less painful.

# Markdown
Up until now I have more or less made my markdown documents with no formatting. I've begun using some formatting to make my documents more readable. Something that has helped with this is using VSCode. I found that when editing a markdown file in VSCode the run button gets replaced by a preview button which lets you preview your markdown file in one tab while editing in the other. I'm now one step closer to whatever this crazy text editing setup is at 1:18

[**Reprinting Classical Lost Books: LindyPress.net** -Luke Smith](https://youtu.be/49ASUFQgWZE)

# VSCode multiple cursors
This program contains a lot of repetivitve code. This is not only annoying to write, but also to change later. Thankfully, with the help of VSCode's multi cusor feature I was able to write and edit multiple lines at once. My favorite hotkey was ctrl + d (different on MacOS). The function of which is to "Add Selection To Next Find Match".