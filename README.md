# Typing Trainer

Typing trainer made in pygame.

This was primarily created to practice OOP but turned into quite a fun little game!

![typing-title](https://user-images.githubusercontent.com/10836434/88630632-cd8eea80-d0a8-11ea-84db-550f93e2ef04.png)
![typing-game](https://user-images.githubusercontent.com/10836434/88630638-cf58ae00-d0a8-11ea-82f4-32c1f240ce2c.png)
![typing-end](https://user-images.githubusercontent.com/10836434/88630640-cff14480-d0a8-11ea-8e86-0fc8f0d8710f.png)

## Setup

Install the required packages from requirements.txt

```
pip install -r requirements.txt
```

Create your own word list and name it words.txt. Put it in the same directory as typing_trainer.py or use one of the sample word lists in samples/

## Usage

Simply run typing_trainer.py

```bash
python3 typing_trainer.py
```

## Options

For now, configuration is done inside typing_trainer.py file itself. At the top of the file there are a number of options for changing things like screen height/width, min & max word length, number of words per second etc. Have a look and play around!

## Roadmap
- Create a more interesting title screen.
- Add difficultly levels. These will be presets of words per second, speed and word length.
- Add a user friendly way to change the game options.

## Contributions

Pull requests & feedback are more than welcome. Please get in touch first if you intend to make any major changes.

## Acknowledgements

Many thanks to:
- [@JDWasabi](https://twitter.com/JDWasabi) for the awesome [game sounds](https://jdwasabi.itch.io/8-bit-16-bit-sound-effects-pack)
