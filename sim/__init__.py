"""The arena: a 5e combat simulator for the character sheets in ../sheets.

The roster is loaded by importing the last module in the chain; each module
imports the one before it and adds (and sometimes patches) one character.
Importing `sim.roster` gives you MAKERS, DANGER, Fight and the dice."""
