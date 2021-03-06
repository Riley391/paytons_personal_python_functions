import pandas as pd
from selenium import webdriver
import time

def remove_list_item(*, the_list, the_item):

  new_list = [item for item in the_list if item != the_item]
  return new_list
  
def plot_x_by_class_y(*, table, x_column, y_column):
  assert isinstance(table, pd.core.frame.DataFrame), f'table is not a dataframe but instead a {type(table)}'
  assert x_column in table.columns, f'unrecognized column: {x_column}. Check spelling and case.'
  assert y_column in table.columns, f'unrecognized column: {y_column}. Check spelling and case.'
  assert table[y_column].nunique()<=5, f'y_column must be of 5 categories or less but has {table[y_column].nunique()}'

  pd.crosstab(table[x_column], table[y_column]).plot(kind='bar', figsize=(15,8), grid=True, logy=True)
  return None

def watch_this_youtube_video(*, url):

  browser = webdriver.Firefox()

  browser.get('https://www.youtube.com/watch?v=BVG86ppZ67w&t=1s')
  vidButton = browser.find_element_by_class_name('ytp-large-play-button')
  #muteButton = browser.find_element_by_class_name('ytp-mute-button')
  time.sleep(5)
  type(vidButton)
  vidButton.click()
  #type(muteButton)
  #muteButton.click()
  time.sleep(120)

  for i in range(1000):
    print('Page viewed ' + str(i + 1) + ' times.')
    browser.get('https://www.youtube.com/watch?v=BVG86ppZ67w&t=1s')
    time.sleep(120)
    i = i + 1
  print('All done.')
  
  return None

def add_these_numbers(*, first, second):
  result = first + second
  print(result)
  return None
