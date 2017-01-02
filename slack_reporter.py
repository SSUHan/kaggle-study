from slacker import Slacker
import datetime

# token = 'xoxb-78078516807-l1lQSr8NsEYj7QthIpUsK4Wq' # gaemigo : bot-test channel
# token = 'xoxb-84340392404-vdDhFPlPIj6M3utfqd3cTvyd' # gaemigo : general channel
token = 'xoxb-122392848899-7J63Xo57XzcJfieZScFmvEnQ' # soma 2level : notify channel
channel_name = 'notify'

slack = Slacker(token)

d = datetime.date.today()
print(type(d))
current_date = d.isoformat()
print(current_date)


attachments_dict = dict()

to_text = "슬랙연결 테스트"
attachments_dict['pretext'] = "슬랙연결 pretext" # pretext:attachment 블록전에 나타나는 text
attachments_dict['title'] = "트레이닝 종료"
attachments_dict['title_link'] = "http://115.68.116.16/swmaestro/reservation_status.html"
attachments_dict['fallback'] = "트레이닝 종료알림"
attachments_dict['text'] = to_text
attachments_dict['mrkdwn_in'] = ['text', 'pretext']
print("slack 에서 요청에 답을 합니다")

attachments = [attachments_dict]
slack.chat.post_message(channel_name, text=None, attachments=attachments, as_user=True)
print("응답을 종료합니다")