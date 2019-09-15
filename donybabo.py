import discord
import random

client = discord.Client()

Token = 'NjIyMDc2MDA2NTI5NzYxMzEz.XXzDfA.u5M5C3V3XDIJ5aEOkiBPJI-PN8A'

@client.event
async def on_ready():
	#봇이 처음 준비되면
	print(client.user.id)
	print('READY')#콘솔에 실행됐다고 표시해줌...사실없어도 되는데
	game = discord.Game("봇 공부중/~명령어")#게임중 상태를 저장하는 변수
	await client.change_presence(status=discord.Status.online, activity=game)#디코에서 상태를 온라인으로 바꿔주고 게임 상태를 띄움

@client.event
async def on_message(message):
	#메시지가 오면
	if message.content.startswith('~뭐해'):
		rand = random.randint(1,2)
		if rand == 1:
			await message.channel.send("공부")
		if rand == 2:
			await message.channel.send("게임")
		
	if message.content.startswith('~윤성이'):
		await message.channel.send("좋음")

	if message.content.startswith('~인구'):
		await message.channel.send("먹을거 좋아함")

	if message.content.startswith('~뭐하지?'):
		rand = random.randint(1,5)
		if rand == 1:
			await message.channel.send("카트")
		if rand == 2:
			await message.channel.send("카트")
		if rand == 3:
			await message.channel.send("마크")
		if rand == 4:
			await message.channel.send("옵치")
		if rand == 5:
			await message.channel.send("끄투")

	if message.content .startswith('~마크'):
		await message.channel.send("갓겜")

	if message.content.startswith('~오버워치'):
		await message.channel.send("옵치갓겜 때문에 평범한겜")

	if message.content.startswith('~카트'):
		await message.channel.send("많이 뿌려서 갓겜")

	if message.content.startswith('~끄투'):
		await message.channel.send("친구랑하면 갓겜")

	if message.content.startswith('~이스터에그'):
		await message.channel.send("이걸 찾다니 대박 (힌트: 이??애?+명령어)")

	if message.content.startswith('~이스터애그 명령어'):
		await message.channel.send("이거는 맞추라고 한거임 (힌트: 게임 +힌트 ")

	if message.content.startswith('~끄투 힌트'):
		await message.channel.send("약빤게임(힌트: ??체널 (이 메세지 안에 있음))")

	if message.content.startswith('~약빤체널'):
		await message.channel.send("https://www.youtube.com/channel/UCxbxK61xeFoymuxmi4ik73g   (~이스터에he 목록)")

	if message.content.startswith('~이미 삭제된 명령어 입니다'):
		await message.channel.send("삭제")

	if message.content.startswith('~윤성바보'):
		await message.channel.send("ㅇㅈ")

	if message.content.startswith('~한조'):
		await message.channel.send("망할")

	if message.content.startswith('게임'):
		await message.channel.send("재밋음")

	if message.content.startswith('ㅋ'):
		await message.channel.send("'ㅋㅋㅋㅋ'")

	if message.content.startswith('~게임'):
			await message.channel.send("꿀잼")

	if message.content.startswith('~옵치케릭'):
		rand = random.randint(1,30)
		if rand == 1:
			await message.channel.send("디바")
		if rand == 2:
			await message.channel.send("라인")
		if rand == 3:
			await message.channel.send("레킹볼")
		if rand == 4:
			await message.channel.send("로드호그")
		if rand == 5:
			await message.channel.send("시그마")
		if rand == 5:
			await message.channel.send("오리사")
		if rand == 6:
			await message.channel.send("윈스턴")
		if rand == 7:
			await message.channel.send("자리아")
		if rand == 8:
			await message.channel.send("겐지")
		if rand == 9:
			await message.channel.send("둠발놈")
		if rand == 10:
			await message.channel.send("찐퍼")
		if rand == 11:
			await message.channel.send("맥크리")
		if rand == 12:
			await message.channel.send("메이코페스")
		if rand == 13:
			await message.channel.send("바스티온")
		if rand == 14:
			await message.channel.send("게이(솔저)")
		if rand == 15:
			await message.channel.send("솜브라")
		if rand == 16:
			await message.channel.send("시메트라")
		if rand == 17:
			await message.channel.send("애쉬")
		if rand == 18:
			await message.channel.send("적페메이커")
		if rand == 19:
			await message.channel.send("정크랫")
		if rand == 20:
			await message.channel.send("토르비온")
		if rand == 21:
			await message.channel.send("트레이서")
		if rand == 22:
			await message.channel.send("파라")
		if rand == 23:
			await message.channel.send("킹조")
		if rand == 24:
			await message.channel.send("루시우")
		if rand == 25:
			await message.channel.send("메르시")
		if rand == 26:
			await message.channel.send("모이라")
		if rand == 27:
			await message.channel.send("바티스트")
		if rand == 28:
			await message.channel.send("브리기테")
		if rand == 29:
			await message.channel.send("아나")
		if rand == 30:
			await message.channel.send("젠야타")

	if message.content.startswith('~명령어'):
		embed = discord.Embed(
			title = "명령어",
			description = "~이스터에그 있음",
			colour = discord.Colour.blue()
			) #디스코드에 embed를 embed 변수에 저장해서 값을 바꿔줌
		embed.add_field(name = "~뭐해", value = "공부 혹은 게임으로 답함")
		#만든 embed에 내용을 추가함. name = 제목 value = 그 밑에 뜨는거
		embed.add_field(name = "~뭐하지?", value = "마크, 옵치, 카트, 뜨투중 하나 추천함")
		embed.add_field(name = "~게임", value = "재밋음")
		embed.add_field(name = "~옵치케릭", value = "옵치케릭중 하나를 골라 추천")
		embed.add_field(name = "~이미 삭제된 명령어 입니다", value = "버그로 인해 삭제")
		embed.add_field(name = "~한조", value = "처보삼")
		embed.add_field(name = "~끄투", value = "끄투에 대한 겜 평가")
		embed.add_field(name = "~카트", value = "카트에 대한 겜 평가")
		embed.add_field(name = "~오버워치", value = "오버뭐치에 대한 겜 평가")
		embed.add_field(name = "~마크", value = "마크에 대한 겜 평가")
		await message.channel.send(embed=embed)

	if message.content.startswith('~이스터에he 목록'):
		embed = discord.Embed(
			title = "이스터에그 목록",
			description = "와 다찾냐이걸",
			colour = discord.Colour.blue()
			) #디스코드에 embed를 embed 변수에 저장해서 값을 바꿔줌
		embed.add_field(name = "~끄투 힌트", value = "힌트를 주기위한 명령어")
		#만든 embed에 내용을 추가함. name = 제목 value = 그 밑에 뜨는거
		embed.add_field(name = "~윤성이", value = "좋음 이라 뜸")
		embed.add_field(name = "~인구", value = "먹을거 좋아함 이라 뜸")
		embed.add_field(name = "~약빤체널", value = "표림 유튜브 주소")
		embed.add_field(name = "~이스터에그", value = "힌트를 주기위한 명령어2")
		embed.add_field(name = "~이스터애그 명령어", value = "힌트를 주기위한 명령어3")
		embed.add_field(name = "~이스터에he 목록", value = "지금 실행중인거")
		await message.channel.send(embed=embed) #그 embed를 메시지로 보냄.	

client.run(Token)#token값을 토큰으로 봇을 실행함
