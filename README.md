# CLICalc

Basicalc is a very basic, CLI based calculator. Due to current limitations,you can only solve equations with two numbers in them at a time.

## Installation

To install the program, use the git clone command in the terminal of your choice.

```bash
git clone https://github.com/Alexosterrieth/basicalc.git
```

Change to the working directory of Basicalc.

```bash
cd basicalc
```

You are done installing Basicalc. In the event you close your terminal, you may need to type in 'cd basicalc' again in order to return to the working directory.

## Usage

Before running the program, you must have Python3 installed. Please reffer to online tutorials for installation instructions.

To start the program, type the following command:

```bash
python3 basicalc.py
```

The program will promt you to chose the type of operation you want to solve. Type in the corresponding number and press enter.

The following should serve as the formulas used to know the order in which to type in the numbers:
- final result = first number + second number
- final result = first number - second number
- final result = first number x second number
- final result = first number / second number
When prompted to type in the first number, type it in and press enter. Repeat for the second number.

Once the final result is shown, you will be asked whether you have more calculation to make.
Type in "yes"/"y", or "no"/"n" depending on your preference.
The program will automatically close if you type in "no".

## Uninstall

To uninstall the program, go to the parent directory of CLICalc's working directory. For most people, type in:

```bash
cd ~
```

Then type:

```bash
sudo rm -r clicalc
```

You may be promted to type in your password.

## License

This software uses the [GNU General Public License V3.0](https://www.gnu.org/licenses/gpl-3.0.html)