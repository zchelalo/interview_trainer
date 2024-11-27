from gtts import gTTS
from playsound import playsound

import random
import os
import curses

language = 'en'

questions = [
  {
    "question": "Are you the best person for this job? Why?",
    "already_answered": False
  },
  {
    "question": "Describe a difficult experience at work and how you handled it.",
    "already_answered": False
  },
  {
    "question": "Describe yourself.",
    "already_answered": False
  },
  {
    "question": "Describe your best boss and your worst boss.",
    "already_answered": False
  },
  {
    "question": "Give some examples of teamwork.",
    "already_answered": False
  },
  {
    "question": "How do you handle pressure?",
    "already_answered": False
  },
  {
    "question": "How do you measure success?",
    "already_answered": False
  },
  {
    "question": "How long do you expect to work for this company?",
    "already_answered": False
  },
  {
    "question": "How much do you expect to get paid?",
    "already_answered": False
  },
  {
    "question": "Is there a type of work environment you prefer?",
    "already_answered": False
  },
  {
    "question": "Tell me why you want to work here.",
    "already_answered": False
  },
  {
    "question": "What are you passionate about?",
    "already_answered": False
  },
  {
    "question": "What are your goals for the future?",
    "already_answered": False
  },
  {
    "question": "What can you do for this company?",
    "already_answered": False
  },
  {
    "question": "What did you like or dislike about your previous job?",
    "already_answered": False
  },
  {
    "question": "What problems have you encountered at work?",
    "already_answered": False
  },
  {
    "question": "What relevant experience do you have?",
    "already_answered": False
  },
  {
    "question": "Why do you want this job?",
    "already_answered": False
  },
  {
    "question": "Why should we hire you?",
    "already_answered": False
  },
  {
    "question": "What do you know about this company?",
    "already_answered": False
  }
]

def get_question():
  questions_size = len(questions)
  random_index = random.randrange(questions_size)
  return questions[random_index]

def get_unanswered_question():
  unanswered_questions = list(filter(lambda question: not question["already_answered"], questions))
  unanswered_questions_size = len(unanswered_questions)
  if unanswered_questions_size == 0:
    return None
  random_index = random.randrange(unanswered_questions_size)
  return unanswered_questions[random_index]

def speak_string(text):
  tts = gTTS(text=text, lang=language)
  audio_file = "text.mp3"
  tts.save(audio_file)
  playsound(audio_file)
  os.remove(audio_file)

def main(stdscr):
  speak_string("Welcome to the interview question generator!")
  stdscr.clear()
  stdscr.refresh()

  while True:
    question = get_unanswered_question()
    if question is None:
      speak_string("All questions have been answered.")
      break
    speak_string(question["question"])
    question["already_answered"] = True

    stdscr.clear()
    stdscr.addstr("Press Enter to get the next question.\n")
    stdscr.refresh()

    key = stdscr.getch()
    if key == 10:
      continue

if __name__ == "__main__":
  curses.wrapper(main)