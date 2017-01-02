from slacker import Slacker
import datetime


def send_message_slack(title, contents, type='training-finish' ,token='xoxb-122392848899-7J63Xo57XzcJfieZScFmvEnQ', channel_name='notify'):

    # token = 'xoxb-78078516807-l1lQSr8NsEYj7QthIpUsK4Wq' # gaemigo : bot-test channel
    # token = 'xoxb-84340392404-vdDhFPlPIj6M3utfqd3cTvyd' # gaemigo : general channel
    # token = 'xoxb-122392848899-7J63Xo57XzcJfieZScFmvEnQ' # soma 2level : notify channel
    # channel_name = 'notify'

    slack = Slacker(token)

    d = datetime.date.today()

    current_date = d.isoformat()
    print(current_date)

    attachments_dict = dict()

    to_text = contents
    if type=='training-finish':
        pretext = current_date +' 트레이닝이 종료되었습니다'
        fallback = '트레이닝 종료알림'
    else:
        pretext = '정의된 타입이 없습니다'
        fallback = 'fallback'

    attachments_dict['pretext'] = pretext # pretext:attachment 블록전에 나타나는 text
    attachments_dict['title'] = title
    # attachments_dict['title_link'] = "http://115.68.116.16/swmaestro/reservation_status.html"
    attachments_dict['fallback'] = fallback
    attachments_dict['text'] = to_text
    attachments_dict['mrkdwn_in'] = ['text', 'pretext']
    print("slack 에서 요청에 답을 합니다")

    attachments = [attachments_dict]
    slack.chat.post_message(channel_name, text=None, attachments=attachments, as_user=True)
    print("응답을 종료합니다")


if __name__ == '__main__':
    send_message_slack('트레이닝 종료', '이러이러한 트레이닝이 종료되었다! 확인부탁', type='training-finish')