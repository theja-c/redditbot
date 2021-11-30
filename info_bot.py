import praw
import time

reddit = praw.Reddit(
    client_id="llfFvcA94j1jTme_3IQ4lw",
    client_secret="xazDtLezH1l187eWSq2JqRfbUgkMAA",
    user_agent='<console:info:1.0>',
    username='info_bot32145',
    password='pass32145')
subreddit =reddit.subreddit("television")
stock_info =["info Bot here!! This website does provide some reliable stock infos -https://finance.yahoo.com/ "]
#happy_info=["info Bot here!! need good news This website provides happy and good news infos-https://www.goodnewsnetwork.org/"]
for submission in subreddit.hot(limit=10):
  #to print a title
  #print("**************")
  #print(submission.title)

  for comment in submission.comments:
    if hasattr(comment,"body"):
      comment_lower=comment.body.lower()
      #if "happy" in comment_lower:
      if "stock" in comment_lower:
        print("--------")
        print(comment.body)
        comment.reply(stock_info)
        #for reply to happy in comments
        #comment.reply(happy_info)
        time.sleep(680)