# psychopy-rdk-discrimination

A simple perceptual discrimination experiment following the dot motion paradigm. This experiment was built to demonstrate some basic features of the PsychoPy Builder. It is much inspired by the study _Bias in the Brain: A Diffusion model Analysis of Prior Probability and Potential Payoff_ by Mulder et al. (2012), while only implementing prior probability manipulation but not potential payoff.

## Experiment

The experiment consists of instructions, some blocks of trials and a debriefing. The instructions and debriefing are simple screens with text, while the trials (and the trial blocks) are a bit more complicated.

#### A trial

First, a fixation cross is shown for either 100ms, 350ms, 800ms or 1200ms. The actual duration is randomized for each trial. Such a randomization cannot be done using the user interface, but requires a small piece of Python code. Check out the code block of the *Fixation_pre_cue* routine to learn how this can be achieved.

Next, a cue is presented for 1000ms. It can be either an arrow pointing to the right, an arrow pointing to the left or a simple circle (for the control condition). The code block in the *Cue* routine sets the actual cue for each trial based on the loop variable **cue** (more on that later).

After the cue, another fixation cross is presented - this time for either 3400ms, 4000ms, 4500ms or 5000ms. As with the first fixation cross, the actual duration is randomly chosen.

Following the second fixation cross, the stimulus itself is displayed for 1500ms: a *random dot kinematogram*. Its dots are moving either to the right or the left at a coherence level of 8%. The movement direction of a single trial is determined by the loop variable **direction**, and set in the code block of the *Dots* routine. Participants have to decide which direction the perceive, and can log in their response by pressing either the left arrow key or the right arrow key on the keyboard.

Finally, a feedback screen is shown. If the participant responded within the first 100ms, the words "too fast" are displayed. If no response was logged in during the whole stimulus, the word "miss" is displayed. If the response was correct, "+5 points" is displayed and if it was wrong "+0 points* is displayed.

#### The *main_blocks_loop*

With _loops_ in PsychoPy we have the possibility to repeat one or more routines. In this experiment, this is used to show the same trial (as described above) multiple times, but each time with different values for the _loop variables_. So a loop repeats a trial for some times, changing the loop variables with each repetition. The trial itself, in turn, reads those loop variables to know, for example, whether the dots should move to the right or to the left. Here, only the *main_blocks_loop* is explained, but the principle applies to the *practice_block_loop* as well.

To define the different values for the loop variables, we have to create a simple csv file:

```csv
cue,direction
left,right
left,left
none,right
...
```

This csv file (the conditions file) defines the two loop variables *cue* and *direction*. The cue can be either _left_, _right_ or _none_, while the direction can be _left_ or _right_.

In the user interface, we can specify the `loopType` and `nReps` variables for the loop when we click on it. With the former we can control, if we want to, e.g., shuffle the rows in the condition file or run them sequentially from top to bottom, while the latter defines how many times each row of the conditions file should be repeated.

For the *main_blocks_loop* we have a conditions file with 80 rows corresponding to 40 neutral trials and 40 biased trials. In one half of the neutral trials the dots move to the right, in the other half they move to the left. In the biased trials, 32 of the cues are valid (i.e. coherent with the dot movement direction) and 16 are invalid, while for both valid and invalid cues the dots move to the right in 50% of trials and to the left in the other 50% of trials.

The `nReps` variable is set to `2`, resulting in all those rows being run twice (160 trials in total) and the `loopType` variable is set to `random`, resulting in the trials being run in random order.
