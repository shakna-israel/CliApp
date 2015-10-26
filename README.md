# CliApp

A framework for building command-line tools with Python.

---

I often find myself having to build commandline interfaces with the various Python tools I build for work.

Frustrated with the lack of libraries, and the lack of flexibility in the few that exist, I have begun to build my own.

***This is not yet production ready!***

Currently, CliApp can be run as follows:

```python
import cliapp

app = cliapp.CliApp()
print(app.display_titles(["List","Of","Categories"], "|"))
print(app.display_line(["List","Of","Items"],"|"))
```

CliApp can also guess, fairly well, how big your console is, and try and ensure everything you want to output can fit.

Currently, only ```display_titles``` will attempt to change this.

You can either set the maximum_width, and the number of items to fit, like so:

```python
import cliapp

app = cliapp.CliApp()
app.maximum_width = 180
app.cell_width = 20
app.cell_no = 6
```

Or allow CliApp to guess for you:

```python
import cliapp

app = cliapp.CliApp()
app.cell_no = 6
app.guess_widths()
```

**Note**: CliApp will not guess the number of cells you need normally. (```display_titles``` being the exception).

### License

MIT License, see [LICENSE](LICENSE)

### Contributing

This project is fairly raw, so if you find a way to fix my math, or have a suggestion, feel free to create a pull request or an issue.

However, I may or may not ask for it to be tweaked, to fit it more concisely with the direction CliApp is moving in.

