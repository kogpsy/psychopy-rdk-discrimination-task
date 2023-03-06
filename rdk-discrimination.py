#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.1.0),
    on Mon Mar  6 21:56:53 2023
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

import psychopy
psychopy.useVersion('2023.1.0')


# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# Run 'Before Experiment' code from code
import time, string, random

# sample 3 uppercase letters
letters = np.random.choice(list(string.ascii_uppercase), 3)
# convert characters into string
letters = ''.join(letters)

# take timestamp in seconds and convert to milliseconds
timestamp = round(time.time() * 1000)
# remove first 6 digits
timestamp = int(str(timestamp)[6:])
# concatenate letters and timestamp to create unique ID
participant_id = letters + str(timestamp)


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2023.1.0'
expName = 'rdk-discrimination'  # from the Builder filename that created this script
expInfo = {
    'Pseudonym': partipant_id,
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['Pseudonym'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/andrew/Library/CloudStorage/OneDrive-UniversitaetBern/teaching/neuroscicomplabFS23/psychopy-rdk-discrimination-task/rdk-discrimination.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[2056, 1329], fullscr=True, screen=-1, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    backgroundImage='', backgroundFit='none',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "participant_id" ---

# --- Initialize components for Routine "Instruction" ---
instruction_text = visual.TextStim(win=win, name='instruction_text',
    text="Welcome to the experiment.\n\nIn the following you will solve a series of tasks. You will be presented with a circle full of dots. Some of these dots will be moving to either the left or to the right. Your task is to decide in which direction they are moving.\n\nPress the [ F key ] if you think the dots are moving to the left, or the [ J key] if you think they are moving the right.\n\nBefore the dots appear, you will see an arrow on the screen indicating the more probable direction of motion. If the arrow points to the right, the dots are more likely to move to the right than to the left, and vice versa.\n\nPlease always focus on the small cross on the screen, if nothing else is presented, and try to respond as fast as possible.\n\nPress [ space ] to start with some practice runs when you're ready.",
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
instruction_keyboard_response = keyboard.Keyboard()

# --- Initialize components for Routine "ISI" ---
static_isi = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='static_isi')

# --- Initialize components for Routine "Fixation_pre_cue" ---
fixation_pre = visual.TextStim(win=win, name='fixation_pre',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "Cue" ---
image = visual.ImageStim(
    win=win,
    name='image', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.2, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# --- Initialize components for Routine "Fixation_post_cue" ---
fixation_post = visual.TextStim(win=win, name='fixation_post',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "Dots" ---
dots_background = visual.ShapeStim(
    win=win, name='dots_background',
    size=(0.75, 0.75), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=-1.0, interpolate=True)
dots_stimulus = visual.DotStim(
    win=win, name='dots_stimulus',
    nDots=250, dotSize=3.0,
    speed=0.0125, dir=1.0, coherence=0.08,
    fieldPos=(0.0, 0.0), fieldSize=0.75, fieldAnchor='center', fieldShape='circle',
    signalDots='same', noiseDots='walk',dotLife=3.0,
    color=[1.0,1.0,1.0], colorSpace='rgb', opacity=1.0,
    depth=-2.0)
dots_keyboard_response = keyboard.Keyboard()

# --- Initialize components for Routine "Feedback" ---
feedback_text = visual.TextStim(win=win, name='feedback_text',
    text='',
    font='Open Sans',
    pos=(0, 0.01), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "Instruction_Main" ---
instruction_main_text = visual.TextStim(win=win, name='instruction_main_text',
    text='We are now finished with the practice runs and will proceed to the main experiment.\n\nPlease try to respond as fast as possible.\n\nPress [ space ] to start the main experiment.',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
instruction_main_keyboard_response = keyboard.Keyboard()

# --- Initialize components for Routine "ISI" ---
static_isi = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='static_isi')

# --- Initialize components for Routine "Fixation_pre_cue" ---
fixation_pre = visual.TextStim(win=win, name='fixation_pre',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "Cue" ---
image = visual.ImageStim(
    win=win,
    name='image', 
    image='default.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.2, 0.1),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# --- Initialize components for Routine "Fixation_post_cue" ---
fixation_post = visual.TextStim(win=win, name='fixation_post',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "Dots" ---
dots_background = visual.ShapeStim(
    win=win, name='dots_background',
    size=(0.75, 0.75), vertices='circle',
    ori=0.0, pos=(0, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=-1.0, interpolate=True)
dots_stimulus = visual.DotStim(
    win=win, name='dots_stimulus',
    nDots=250, dotSize=3.0,
    speed=0.0125, dir=1.0, coherence=0.08,
    fieldPos=(0.0, 0.0), fieldSize=0.75, fieldAnchor='center', fieldShape='circle',
    signalDots='same', noiseDots='walk',dotLife=3.0,
    color=[1.0,1.0,1.0], colorSpace='rgb', opacity=1.0,
    depth=-2.0)
dots_keyboard_response = keyboard.Keyboard()

# --- Initialize components for Routine "Feedback" ---
feedback_text = visual.TextStim(win=win, name='feedback_text',
    text='',
    font='Open Sans',
    pos=(0, 0.01), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "Debriefing" ---
debriefing_text = visual.TextStim(win=win, name='debriefing_text',
    text='Thank you for your participation!\n\nPress [ space ] to end the experiment.',
    font='Open Sans',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
debriefing_keyboard_response = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "participant_id" ---
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
participant_idComponents = []
for thisComponent in participant_idComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "participant_id" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in participant_idComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "participant_id" ---
for thisComponent in participant_idComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "participant_id" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Instruction" ---
continueRoutine = True
# update component parameters for each repeat
instruction_keyboard_response.keys = []
instruction_keyboard_response.rt = []
_instruction_keyboard_response_allKeys = []
# keep track of which components have finished
InstructionComponents = [instruction_text, instruction_keyboard_response]
for thisComponent in InstructionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Instruction" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruction_text* updates
    
    # if instruction_text is starting this frame...
    if instruction_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruction_text.frameNStart = frameN  # exact frame index
        instruction_text.tStart = t  # local t and not account for scr refresh
        instruction_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruction_text, 'tStartRefresh')  # time at next scr refresh
        # update status
        instruction_text.status = STARTED
        instruction_text.setAutoDraw(True)
    
    # if instruction_text is active this frame...
    if instruction_text.status == STARTED:
        # update params
        pass
    
    # *instruction_keyboard_response* updates
    waitOnFlip = False
    
    # if instruction_keyboard_response is starting this frame...
    if instruction_keyboard_response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruction_keyboard_response.frameNStart = frameN  # exact frame index
        instruction_keyboard_response.tStart = t  # local t and not account for scr refresh
        instruction_keyboard_response.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruction_keyboard_response, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instruction_keyboard_response.started')
        # update status
        instruction_keyboard_response.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instruction_keyboard_response.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instruction_keyboard_response.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instruction_keyboard_response.status == STARTED and not waitOnFlip:
        theseKeys = instruction_keyboard_response.getKeys(keyList=['space'], waitRelease=False)
        _instruction_keyboard_response_allKeys.extend(theseKeys)
        if len(_instruction_keyboard_response_allKeys):
            instruction_keyboard_response.keys = _instruction_keyboard_response_allKeys[-1].name  # just the last key pressed
            instruction_keyboard_response.rt = _instruction_keyboard_response_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Instruction" ---
for thisComponent in InstructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practice_block_loop = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions_practice.csv'),
    seed=None, name='practice_block_loop')
thisExp.addLoop(practice_block_loop)  # add the loop to the experiment
thisPractice_block_loop = practice_block_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPractice_block_loop.rgb)
if thisPractice_block_loop != None:
    for paramName in thisPractice_block_loop:
        exec('{} = thisPractice_block_loop[paramName]'.format(paramName))

for thisPractice_block_loop in practice_block_loop:
    currentLoop = practice_block_loop
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_block_loop.rgb)
    if thisPractice_block_loop != None:
        for paramName in thisPractice_block_loop:
            exec('{} = thisPractice_block_loop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "ISI" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    ISIComponents = [static_isi]
    for thisComponent in ISIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ISI" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *static_isi* period
        
        # if static_isi is starting this frame...
        if static_isi.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            static_isi.frameNStart = frameN  # exact frame index
            static_isi.tStart = t  # local t and not account for scr refresh
            static_isi.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(static_isi, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('static_isi.started', t)
            # update status
            static_isi.status = STARTED
            static_isi.start(60*frameDur)
        elif static_isi.status == STARTED:  # one frame should pass before updating params and completing
            static_isi.complete()  # finish the static period
            static_isi.tStop = static_isi.tStart + 60*frameDur  # record stop time
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ISI" ---
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    
    # --- Prepare to start Routine "Fixation_pre_cue" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from fixation_pre_set_duration
    # Before the fixation cross (the one before the cue) is displayed, randomly
    # choose a duration for it. Since we are using seconds as time unit, these
    # numbers correspond to 100ms, 350ms, 800ms and 1200ms.
    fixation_duration_pre_cue = randchoice([0.1, 0.35, 0.8, 1.2])
    # keep track of which components have finished
    Fixation_pre_cueComponents = [fixation_pre]
    for thisComponent in Fixation_pre_cueComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Fixation_pre_cue" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation_pre* updates
        
        # if fixation_pre is starting this frame...
        if fixation_pre.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_pre.frameNStart = frameN  # exact frame index
            fixation_pre.tStart = t  # local t and not account for scr refresh
            fixation_pre.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_pre, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation_pre.started')
            # update status
            fixation_pre.status = STARTED
            fixation_pre.setAutoDraw(True)
        
        # if fixation_pre is active this frame...
        if fixation_pre.status == STARTED:
            # update params
            pass
        
        # if fixation_pre is stopping this frame...
        if fixation_pre.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_pre.tStartRefresh + fixation_duration_pre_cue-frameTolerance:
                # keep track of stop time/frame for later
                fixation_pre.tStop = t  # not accounting for scr refresh
                fixation_pre.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_pre.stopped')
                # update status
                fixation_pre.status = FINISHED
                fixation_pre.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Fixation_pre_cueComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Fixation_pre_cue" ---
    for thisComponent in Fixation_pre_cueComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "Fixation_pre_cue" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Cue" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from cue_set_text
    # Here we set which cue is displayed (a cue is just a text symbol). We check the
    # content of the loop variable 'cue', and decide if the cue text should be an
    # arrow pointing the left, an arrow pointing to the right or just a circle.
    if cue == "left":
        cue_path = "img/arrow_left.png"
    elif cue == "right":
        cue_path = "img/arrow_right.png"
    elif cue == "none":
        cue_path = "img/neutral.png"
    image.setImage(cue_path)
    # keep track of which components have finished
    CueComponents = [image]
    for thisComponent in CueComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Cue" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image* updates
        
        # if image is starting this frame...
        if image.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image.started')
            # update status
            image.status = STARTED
            image.setAutoDraw(True)
        
        # if image is active this frame...
        if image.status == STARTED:
            # update params
            pass
        
        # if image is stopping this frame...
        if image.status == STARTED:
            if frameN >= (image.frameNStart + 60):
                # keep track of stop time/frame for later
                image.tStop = t  # not accounting for scr refresh
                image.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image.stopped')
                # update status
                image.status = FINISHED
                image.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in CueComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Cue" ---
    for thisComponent in CueComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    
    # --- Prepare to start Routine "Fixation_post_cue" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from fixation_post_set_duration
    # Before the fixation cross (the one after the cue) is displayed, randomly
    # choose a duration for it. Since we are using seconds as time unit, these
    # numbers correspond to 3400ms, 4000ms, 4500ms and 5000ms.
    fixation_duration_post_cue = randchoice([3.4, 4, 4.5, 5])
    # keep track of which components have finished
    Fixation_post_cueComponents = [fixation_post]
    for thisComponent in Fixation_post_cueComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Fixation_post_cue" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation_post* updates
        
        # if fixation_post is starting this frame...
        if fixation_post.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_post.frameNStart = frameN  # exact frame index
            fixation_post.tStart = t  # local t and not account for scr refresh
            fixation_post.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_post, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation_post.started')
            # update status
            fixation_post.status = STARTED
            fixation_post.setAutoDraw(True)
        
        # if fixation_post is active this frame...
        if fixation_post.status == STARTED:
            # update params
            pass
        
        # if fixation_post is stopping this frame...
        if fixation_post.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_post.tStartRefresh + fixation_duration_post_cue-frameTolerance:
                # keep track of stop time/frame for later
                fixation_post.tStop = t  # not accounting for scr refresh
                fixation_post.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_post.stopped')
                # update status
                fixation_post.status = FINISHED
                fixation_post.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Fixation_post_cueComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Fixation_post_cue" ---
    for thisComponent in Fixation_post_cueComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "Fixation_post_cue" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Dots" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from dots_set_direction
    if direction == "right":
        dots_direction = 0
    elif direction == "left":
        dots_direction = 180
    dots_stimulus.setDir(dots_direction)
    dots_stimulus.refreshDots()
    dots_keyboard_response.keys = []
    dots_keyboard_response.rt = []
    _dots_keyboard_response_allKeys = []
    # keep track of which components have finished
    DotsComponents = [dots_background, dots_stimulus, dots_keyboard_response]
    for thisComponent in DotsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Dots" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *dots_background* updates
        
        # if dots_background is starting this frame...
        if dots_background.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            dots_background.frameNStart = frameN  # exact frame index
            dots_background.tStart = t  # local t and not account for scr refresh
            dots_background.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(dots_background, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'dots_background.started')
            # update status
            dots_background.status = STARTED
            dots_background.setAutoDraw(True)
        
        # if dots_background is active this frame...
        if dots_background.status == STARTED:
            # update params
            pass
        
        # if dots_background is stopping this frame...
        if dots_background.status == STARTED:
            if frameN >= (dots_background.frameNStart + 90):
                # keep track of stop time/frame for later
                dots_background.tStop = t  # not accounting for scr refresh
                dots_background.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'dots_background.stopped')
                # update status
                dots_background.status = FINISHED
                dots_background.setAutoDraw(False)
        
        # *dots_stimulus* updates
        
        # if dots_stimulus is starting this frame...
        if dots_stimulus.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            dots_stimulus.frameNStart = frameN  # exact frame index
            dots_stimulus.tStart = t  # local t and not account for scr refresh
            dots_stimulus.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(dots_stimulus, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'dots_stimulus.started')
            # update status
            dots_stimulus.status = STARTED
            dots_stimulus.setAutoDraw(True)
        
        # if dots_stimulus is active this frame...
        if dots_stimulus.status == STARTED:
            # update params
            pass
        
        # if dots_stimulus is stopping this frame...
        if dots_stimulus.status == STARTED:
            if frameN >= (dots_stimulus.frameNStart + 90):
                # keep track of stop time/frame for later
                dots_stimulus.tStop = t  # not accounting for scr refresh
                dots_stimulus.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'dots_stimulus.stopped')
                # update status
                dots_stimulus.status = FINISHED
                dots_stimulus.setAutoDraw(False)
        
        # *dots_keyboard_response* updates
        waitOnFlip = False
        
        # if dots_keyboard_response is starting this frame...
        if dots_keyboard_response.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            dots_keyboard_response.frameNStart = frameN  # exact frame index
            dots_keyboard_response.tStart = t  # local t and not account for scr refresh
            dots_keyboard_response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(dots_keyboard_response, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'dots_keyboard_response.started')
            # update status
            dots_keyboard_response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(dots_keyboard_response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(dots_keyboard_response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if dots_keyboard_response is stopping this frame...
        if dots_keyboard_response.status == STARTED:
            if frameN >= (dots_keyboard_response.frameNStart + 90):
                # keep track of stop time/frame for later
                dots_keyboard_response.tStop = t  # not accounting for scr refresh
                dots_keyboard_response.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'dots_keyboard_response.stopped')
                # update status
                dots_keyboard_response.status = FINISHED
                dots_keyboard_response.status = FINISHED
        if dots_keyboard_response.status == STARTED and not waitOnFlip:
            theseKeys = dots_keyboard_response.getKeys(keyList=['f','j'], waitRelease=False)
            _dots_keyboard_response_allKeys.extend(theseKeys)
            if len(_dots_keyboard_response_allKeys):
                dots_keyboard_response.keys = _dots_keyboard_response_allKeys[-1].name  # just the last key pressed
                dots_keyboard_response.rt = _dots_keyboard_response_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in DotsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Dots" ---
    for thisComponent in DotsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if dots_keyboard_response.keys in ['', [], None]:  # No response was made
        dots_keyboard_response.keys = None
    practice_block_loop.addData('dots_keyboard_response.keys',dots_keyboard_response.keys)
    if dots_keyboard_response.keys != None:  # we had a response
        practice_block_loop.addData('dots_keyboard_response.rt', dots_keyboard_response.rt)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.500000)
    
    # --- Prepare to start Routine "Feedback" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from feedback_set_text
    # If the participant did not respond at all, set the response text to 'miss'.
    # You can figure that out by checking whether the given response 'None'.
    # 'None' in Python means a values is not defined, so when
    # dots_main_keyboard_resp.keys is 'None' we know the participant did not respond.
    if dots_keyboard_response.keys is None:
        response_text = "miss"
    
    # If the response time (rt) was shorter than 100ms, set the response text to
    # 'too fast' (like Mulder et al., 2012 did).
    # You can get the response time from the Keyboard component that was used to
    # capture the response (name_of_the_keyboard_component.rt).
    elif dots_keyboard_response.rt <= 0.1:
        response_text = "too fast"
    
    # If the response time was between 100ms and 1500ms (i.e. it was valid), give
    # feedback. If the repsonse was also correct, set the response text to '+5 points',
    # if it was wrong, set the response text to '+0 points'.
    # The variable 'direction' is a loop variable storing the stimulus direction for
    # the current trial.
    else:
        if (direction == "left" and dots_keyboard_response.keys == "f" or 
            direction == "right" and dots_keyboard_response.keys == "j"
        ):
            response_text = "+5 points"
        else:
            response_text = "+0 points"
            
    feedback_text.setText(response_text)
    # keep track of which components have finished
    FeedbackComponents = [feedback_text]
    for thisComponent in FeedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Feedback" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedback_text* updates
        
        # if feedback_text is starting this frame...
        if feedback_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback_text.frameNStart = frameN  # exact frame index
            feedback_text.tStart = t  # local t and not account for scr refresh
            feedback_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'feedback_text.started')
            # update status
            feedback_text.status = STARTED
            feedback_text.setAutoDraw(True)
        
        # if feedback_text is active this frame...
        if feedback_text.status == STARTED:
            # update params
            pass
        
        # if feedback_text is stopping this frame...
        if feedback_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback_text.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                feedback_text.tStop = t  # not accounting for scr refresh
                feedback_text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedback_text.stopped')
                # update status
                feedback_text.status = FINISHED
                feedback_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FeedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Feedback" ---
    for thisComponent in FeedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'practice_block_loop'


# --- Prepare to start Routine "Instruction_Main" ---
continueRoutine = True
# update component parameters for each repeat
instruction_main_keyboard_response.keys = []
instruction_main_keyboard_response.rt = []
_instruction_main_keyboard_response_allKeys = []
# keep track of which components have finished
Instruction_MainComponents = [instruction_main_text, instruction_main_keyboard_response]
for thisComponent in Instruction_MainComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Instruction_Main" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruction_main_text* updates
    
    # if instruction_main_text is starting this frame...
    if instruction_main_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruction_main_text.frameNStart = frameN  # exact frame index
        instruction_main_text.tStart = t  # local t and not account for scr refresh
        instruction_main_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruction_main_text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instruction_main_text.started')
        # update status
        instruction_main_text.status = STARTED
        instruction_main_text.setAutoDraw(True)
    
    # if instruction_main_text is active this frame...
    if instruction_main_text.status == STARTED:
        # update params
        pass
    
    # *instruction_main_keyboard_response* updates
    waitOnFlip = False
    
    # if instruction_main_keyboard_response is starting this frame...
    if instruction_main_keyboard_response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instruction_main_keyboard_response.frameNStart = frameN  # exact frame index
        instruction_main_keyboard_response.tStart = t  # local t and not account for scr refresh
        instruction_main_keyboard_response.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruction_main_keyboard_response, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instruction_main_keyboard_response.started')
        # update status
        instruction_main_keyboard_response.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(instruction_main_keyboard_response.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(instruction_main_keyboard_response.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if instruction_main_keyboard_response.status == STARTED and not waitOnFlip:
        theseKeys = instruction_main_keyboard_response.getKeys(keyList=['space'], waitRelease=False)
        _instruction_main_keyboard_response_allKeys.extend(theseKeys)
        if len(_instruction_main_keyboard_response_allKeys):
            instruction_main_keyboard_response.keys = _instruction_main_keyboard_response_allKeys[-1].name  # just the last key pressed
            instruction_main_keyboard_response.rt = _instruction_main_keyboard_response_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instruction_MainComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Instruction_Main" ---
for thisComponent in Instruction_MainComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if instruction_main_keyboard_response.keys in ['', [], None]:  # No response was made
    instruction_main_keyboard_response.keys = None
thisExp.addData('instruction_main_keyboard_response.keys',instruction_main_keyboard_response.keys)
if instruction_main_keyboard_response.keys != None:  # we had a response
    thisExp.addData('instruction_main_keyboard_response.rt', instruction_main_keyboard_response.rt)
thisExp.nextEntry()
# the Routine "Instruction_Main" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
main_blocks_loop = data.TrialHandler(nReps=2.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions.csv'),
    seed=None, name='main_blocks_loop')
thisExp.addLoop(main_blocks_loop)  # add the loop to the experiment
thisMain_blocks_loop = main_blocks_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisMain_blocks_loop.rgb)
if thisMain_blocks_loop != None:
    for paramName in thisMain_blocks_loop:
        exec('{} = thisMain_blocks_loop[paramName]'.format(paramName))

for thisMain_blocks_loop in main_blocks_loop:
    currentLoop = main_blocks_loop
    # abbreviate parameter names if possible (e.g. rgb = thisMain_blocks_loop.rgb)
    if thisMain_blocks_loop != None:
        for paramName in thisMain_blocks_loop:
            exec('{} = thisMain_blocks_loop[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "ISI" ---
    continueRoutine = True
    # update component parameters for each repeat
    # keep track of which components have finished
    ISIComponents = [static_isi]
    for thisComponent in ISIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "ISI" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *static_isi* period
        
        # if static_isi is starting this frame...
        if static_isi.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            static_isi.frameNStart = frameN  # exact frame index
            static_isi.tStart = t  # local t and not account for scr refresh
            static_isi.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(static_isi, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('static_isi.started', t)
            # update status
            static_isi.status = STARTED
            static_isi.start(60*frameDur)
        elif static_isi.status == STARTED:  # one frame should pass before updating params and completing
            static_isi.complete()  # finish the static period
            static_isi.tStop = static_isi.tStart + 60*frameDur  # record stop time
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "ISI" ---
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    
    # --- Prepare to start Routine "Fixation_pre_cue" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from fixation_pre_set_duration
    # Before the fixation cross (the one before the cue) is displayed, randomly
    # choose a duration for it. Since we are using seconds as time unit, these
    # numbers correspond to 100ms, 350ms, 800ms and 1200ms.
    fixation_duration_pre_cue = randchoice([0.1, 0.35, 0.8, 1.2])
    # keep track of which components have finished
    Fixation_pre_cueComponents = [fixation_pre]
    for thisComponent in Fixation_pre_cueComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Fixation_pre_cue" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation_pre* updates
        
        # if fixation_pre is starting this frame...
        if fixation_pre.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_pre.frameNStart = frameN  # exact frame index
            fixation_pre.tStart = t  # local t and not account for scr refresh
            fixation_pre.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_pre, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation_pre.started')
            # update status
            fixation_pre.status = STARTED
            fixation_pre.setAutoDraw(True)
        
        # if fixation_pre is active this frame...
        if fixation_pre.status == STARTED:
            # update params
            pass
        
        # if fixation_pre is stopping this frame...
        if fixation_pre.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_pre.tStartRefresh + fixation_duration_pre_cue-frameTolerance:
                # keep track of stop time/frame for later
                fixation_pre.tStop = t  # not accounting for scr refresh
                fixation_pre.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_pre.stopped')
                # update status
                fixation_pre.status = FINISHED
                fixation_pre.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Fixation_pre_cueComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Fixation_pre_cue" ---
    for thisComponent in Fixation_pre_cueComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "Fixation_pre_cue" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Cue" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from cue_set_text
    # Here we set which cue is displayed (a cue is just a text symbol). We check the
    # content of the loop variable 'cue', and decide if the cue text should be an
    # arrow pointing the left, an arrow pointing to the right or just a circle.
    if cue == "left":
        cue_path = "img/arrow_left.png"
    elif cue == "right":
        cue_path = "img/arrow_right.png"
    elif cue == "none":
        cue_path = "img/neutral.png"
    image.setImage(cue_path)
    # keep track of which components have finished
    CueComponents = [image]
    for thisComponent in CueComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Cue" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image* updates
        
        # if image is starting this frame...
        if image.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image.started')
            # update status
            image.status = STARTED
            image.setAutoDraw(True)
        
        # if image is active this frame...
        if image.status == STARTED:
            # update params
            pass
        
        # if image is stopping this frame...
        if image.status == STARTED:
            if frameN >= (image.frameNStart + 60):
                # keep track of stop time/frame for later
                image.tStop = t  # not accounting for scr refresh
                image.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image.stopped')
                # update status
                image.status = FINISHED
                image.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in CueComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Cue" ---
    for thisComponent in CueComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    
    # --- Prepare to start Routine "Fixation_post_cue" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from fixation_post_set_duration
    # Before the fixation cross (the one after the cue) is displayed, randomly
    # choose a duration for it. Since we are using seconds as time unit, these
    # numbers correspond to 3400ms, 4000ms, 4500ms and 5000ms.
    fixation_duration_post_cue = randchoice([3.4, 4, 4.5, 5])
    # keep track of which components have finished
    Fixation_post_cueComponents = [fixation_post]
    for thisComponent in Fixation_post_cueComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Fixation_post_cue" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation_post* updates
        
        # if fixation_post is starting this frame...
        if fixation_post.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_post.frameNStart = frameN  # exact frame index
            fixation_post.tStart = t  # local t and not account for scr refresh
            fixation_post.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_post, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fixation_post.started')
            # update status
            fixation_post.status = STARTED
            fixation_post.setAutoDraw(True)
        
        # if fixation_post is active this frame...
        if fixation_post.status == STARTED:
            # update params
            pass
        
        # if fixation_post is stopping this frame...
        if fixation_post.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_post.tStartRefresh + fixation_duration_post_cue-frameTolerance:
                # keep track of stop time/frame for later
                fixation_post.tStop = t  # not accounting for scr refresh
                fixation_post.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fixation_post.stopped')
                # update status
                fixation_post.status = FINISHED
                fixation_post.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Fixation_post_cueComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Fixation_post_cue" ---
    for thisComponent in Fixation_post_cueComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "Fixation_post_cue" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Dots" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from dots_set_direction
    if direction == "right":
        dots_direction = 0
    elif direction == "left":
        dots_direction = 180
    dots_stimulus.setDir(dots_direction)
    dots_stimulus.refreshDots()
    dots_keyboard_response.keys = []
    dots_keyboard_response.rt = []
    _dots_keyboard_response_allKeys = []
    # keep track of which components have finished
    DotsComponents = [dots_background, dots_stimulus, dots_keyboard_response]
    for thisComponent in DotsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Dots" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *dots_background* updates
        
        # if dots_background is starting this frame...
        if dots_background.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            dots_background.frameNStart = frameN  # exact frame index
            dots_background.tStart = t  # local t and not account for scr refresh
            dots_background.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(dots_background, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'dots_background.started')
            # update status
            dots_background.status = STARTED
            dots_background.setAutoDraw(True)
        
        # if dots_background is active this frame...
        if dots_background.status == STARTED:
            # update params
            pass
        
        # if dots_background is stopping this frame...
        if dots_background.status == STARTED:
            if frameN >= (dots_background.frameNStart + 90):
                # keep track of stop time/frame for later
                dots_background.tStop = t  # not accounting for scr refresh
                dots_background.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'dots_background.stopped')
                # update status
                dots_background.status = FINISHED
                dots_background.setAutoDraw(False)
        
        # *dots_stimulus* updates
        
        # if dots_stimulus is starting this frame...
        if dots_stimulus.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            dots_stimulus.frameNStart = frameN  # exact frame index
            dots_stimulus.tStart = t  # local t and not account for scr refresh
            dots_stimulus.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(dots_stimulus, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'dots_stimulus.started')
            # update status
            dots_stimulus.status = STARTED
            dots_stimulus.setAutoDraw(True)
        
        # if dots_stimulus is active this frame...
        if dots_stimulus.status == STARTED:
            # update params
            pass
        
        # if dots_stimulus is stopping this frame...
        if dots_stimulus.status == STARTED:
            if frameN >= (dots_stimulus.frameNStart + 90):
                # keep track of stop time/frame for later
                dots_stimulus.tStop = t  # not accounting for scr refresh
                dots_stimulus.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'dots_stimulus.stopped')
                # update status
                dots_stimulus.status = FINISHED
                dots_stimulus.setAutoDraw(False)
        
        # *dots_keyboard_response* updates
        waitOnFlip = False
        
        # if dots_keyboard_response is starting this frame...
        if dots_keyboard_response.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            dots_keyboard_response.frameNStart = frameN  # exact frame index
            dots_keyboard_response.tStart = t  # local t and not account for scr refresh
            dots_keyboard_response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(dots_keyboard_response, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'dots_keyboard_response.started')
            # update status
            dots_keyboard_response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(dots_keyboard_response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(dots_keyboard_response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if dots_keyboard_response is stopping this frame...
        if dots_keyboard_response.status == STARTED:
            if frameN >= (dots_keyboard_response.frameNStart + 90):
                # keep track of stop time/frame for later
                dots_keyboard_response.tStop = t  # not accounting for scr refresh
                dots_keyboard_response.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'dots_keyboard_response.stopped')
                # update status
                dots_keyboard_response.status = FINISHED
                dots_keyboard_response.status = FINISHED
        if dots_keyboard_response.status == STARTED and not waitOnFlip:
            theseKeys = dots_keyboard_response.getKeys(keyList=['f','j'], waitRelease=False)
            _dots_keyboard_response_allKeys.extend(theseKeys)
            if len(_dots_keyboard_response_allKeys):
                dots_keyboard_response.keys = _dots_keyboard_response_allKeys[-1].name  # just the last key pressed
                dots_keyboard_response.rt = _dots_keyboard_response_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in DotsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Dots" ---
    for thisComponent in DotsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if dots_keyboard_response.keys in ['', [], None]:  # No response was made
        dots_keyboard_response.keys = None
    main_blocks_loop.addData('dots_keyboard_response.keys',dots_keyboard_response.keys)
    if dots_keyboard_response.keys != None:  # we had a response
        main_blocks_loop.addData('dots_keyboard_response.rt', dots_keyboard_response.rt)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.500000)
    
    # --- Prepare to start Routine "Feedback" ---
    continueRoutine = True
    # update component parameters for each repeat
    # Run 'Begin Routine' code from feedback_set_text
    # If the participant did not respond at all, set the response text to 'miss'.
    # You can figure that out by checking whether the given response 'None'.
    # 'None' in Python means a values is not defined, so when
    # dots_main_keyboard_resp.keys is 'None' we know the participant did not respond.
    if dots_keyboard_response.keys is None:
        response_text = "miss"
    
    # If the response time (rt) was shorter than 100ms, set the response text to
    # 'too fast' (like Mulder et al., 2012 did).
    # You can get the response time from the Keyboard component that was used to
    # capture the response (name_of_the_keyboard_component.rt).
    elif dots_keyboard_response.rt <= 0.1:
        response_text = "too fast"
    
    # If the response time was between 100ms and 1500ms (i.e. it was valid), give
    # feedback. If the repsonse was also correct, set the response text to '+5 points',
    # if it was wrong, set the response text to '+0 points'.
    # The variable 'direction' is a loop variable storing the stimulus direction for
    # the current trial.
    else:
        if (direction == "left" and dots_keyboard_response.keys == "f" or 
            direction == "right" and dots_keyboard_response.keys == "j"
        ):
            response_text = "+5 points"
        else:
            response_text = "+0 points"
            
    feedback_text.setText(response_text)
    # keep track of which components have finished
    FeedbackComponents = [feedback_text]
    for thisComponent in FeedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Feedback" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedback_text* updates
        
        # if feedback_text is starting this frame...
        if feedback_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback_text.frameNStart = frameN  # exact frame index
            feedback_text.tStart = t  # local t and not account for scr refresh
            feedback_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'feedback_text.started')
            # update status
            feedback_text.status = STARTED
            feedback_text.setAutoDraw(True)
        
        # if feedback_text is active this frame...
        if feedback_text.status == STARTED:
            # update params
            pass
        
        # if feedback_text is stopping this frame...
        if feedback_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback_text.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                feedback_text.tStop = t  # not accounting for scr refresh
                feedback_text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedback_text.stopped')
                # update status
                feedback_text.status = FINISHED
                feedback_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FeedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Feedback" ---
    for thisComponent in FeedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'main_blocks_loop'


# --- Prepare to start Routine "Debriefing" ---
continueRoutine = True
# update component parameters for each repeat
debriefing_keyboard_response.keys = []
debriefing_keyboard_response.rt = []
_debriefing_keyboard_response_allKeys = []
# keep track of which components have finished
DebriefingComponents = [debriefing_text, debriefing_keyboard_response]
for thisComponent in DebriefingComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Debriefing" ---
routineForceEnded = not continueRoutine
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *debriefing_text* updates
    
    # if debriefing_text is starting this frame...
    if debriefing_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        debriefing_text.frameNStart = frameN  # exact frame index
        debriefing_text.tStart = t  # local t and not account for scr refresh
        debriefing_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(debriefing_text, 'tStartRefresh')  # time at next scr refresh
        # update status
        debriefing_text.status = STARTED
        debriefing_text.setAutoDraw(True)
    
    # if debriefing_text is active this frame...
    if debriefing_text.status == STARTED:
        # update params
        pass
    
    # *debriefing_keyboard_response* updates
    waitOnFlip = False
    
    # if debriefing_keyboard_response is starting this frame...
    if debriefing_keyboard_response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        debriefing_keyboard_response.frameNStart = frameN  # exact frame index
        debriefing_keyboard_response.tStart = t  # local t and not account for scr refresh
        debriefing_keyboard_response.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(debriefing_keyboard_response, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'debriefing_keyboard_response.started')
        # update status
        debriefing_keyboard_response.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(debriefing_keyboard_response.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(debriefing_keyboard_response.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if debriefing_keyboard_response.status == STARTED and not waitOnFlip:
        theseKeys = debriefing_keyboard_response.getKeys(keyList=['space'], waitRelease=False)
        _debriefing_keyboard_response_allKeys.extend(theseKeys)
        if len(_debriefing_keyboard_response_allKeys):
            debriefing_keyboard_response.keys = _debriefing_keyboard_response_allKeys[-1].name  # just the last key pressed
            debriefing_keyboard_response.rt = _debriefing_keyboard_response_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in DebriefingComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Debriefing" ---
for thisComponent in DebriefingComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Debriefing" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
