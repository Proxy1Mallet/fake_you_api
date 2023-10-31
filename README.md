<h1 align = "center">ꜰᴀᴋᴇ_ʏᴏᴜ_ᴀᴘɪ</h1>
<details align = "center">
<summary>ʀᴇᴠᴇᴀʟ ᴍᴇ : </summary>

###### This library is intended for requests to the https://fakeyou.com/tts website
###### Эта библиотека предназначена для запросов к https://fakeyou.com/tts
###### example :

```py3
from fake_you import FakeYou
fake_you = FakeYou()
fake_you.login(username_or_email = 'your email or username', password = 'your password')
get_job = fake_you.inference(text = 'your text', model_token = "selected model")
get_path = fake_you.get_job(job_token = get_job.inference_job_token).maybe_public_bucket_wav_audio_path
fake_you.save_waw(path = get_path)
```
</details>

<details align = "center">
<summary>ᴍʏ sᴏᴄɪᴀʟ ɴᴇᴛᴡᴏʀᴋ : </summary>
<br>
<a href = "https://t.me/Proxy1Mallet" target="_blank">
<img src = "https://img.shields.io/badge/ᴛᴇʟᴇɢʀᴀᴍ-92000a?logo=telegram&logoColor=FFFFFF&labelColor=000000">
<a href = "https://discordapp.com/users/875370793100533862/" target="_blank">
<img src = "https://img.shields.io/badge/ᴅɪsᴄᴏʀᴅ-92000a?logo=discord&logoColor=FFFFFF&labelColor=000000">
</br>
</details>
