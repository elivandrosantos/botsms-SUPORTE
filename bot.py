from telebot.async_telebot import AsyncTeleBot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.formatting import hcode
from datetime import datetime
import csv


TOKEN = '6098339666:AAHA0IMgsZlN87Ts6kXhvn1S4NuK_QKy2SQ'

bot = AsyncTeleBot(TOKEN, parse_mode='HTML')

# Dicionário para armazenar IDs de mensagens enviadas
messages = {}


# @bot.message_handler(func=lambda message: True, content_types=[
#     'text', 'animation', 'audio', 'document', 'photo', 'sticker', 'story', 'video', 'video_note', 'voice', 'contact',
#     'dice', 'game', 'poll', 'venue', 'location',  'invoice', 'successful_payment', 'connected_website',
#     'passport_data', 'web_app_data',
# ])
# async def default_command(message):
#     if message.content_type == message.content_type:
#        await bot.send_chat_action(chat_id=message.from_user.id, action='typing')
#        await bot.send_message(message.chat.id, """Não é um comando válido.😕
# Digite /start para interagir com o bot.🤖""")
#        await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)


@bot.message_handler(commands=['start'])
async def start(message):
    chat_id = message.chat.id
    message_id = message.message_id
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton('💰 Financeiro', callback_data='financeiro'),
        InlineKeyboardButton('🛠 Suporte Técnico', callback_data='suporte_tecnico'),
        InlineKeyboardButton('🤖 Bot Explorer', callback_data='bot_explorer'), row_width=1
        )
    markup.add(InlineKeyboardButton('👨‍💻 Admin', url='t.me/ordnavile'))
    markup.add(InlineKeyboardButton('📋 Termos de Uso', url='https://telegra.ph/Termos-de-Uso-07-15'))
    await bot.send_chat_action(chat_id=message.from_user.id, action='typing')
    sent_message = await bot.send_message(chat_id, f"""Seja bem vindo! \n
Sou o <b>Vadox</b> 🧞‍♂️, seu assistente inteligente! 🤖

Por favor, selecione o departamento que melhor atende sua necessidade. 👇 """, reply_markup=markup)

    messages[chat_id] = sent_message.message_id


@bot.callback_query_handler(func=lambda call: call.data == 'start')
async def callback_start(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton('💰 Financeiro', callback_data='financeiro'),
        InlineKeyboardButton('🛠 Suporte Técnico', callback_data='suporte_tecnico'),
        InlineKeyboardButton('🤖 Bot Explorer', callback_data='bot_explorer'), row_width=1

    )
    markup.add(InlineKeyboardButton(' 👨‍💻Admin', url='t.me/ordnavile'))
    markup.add(InlineKeyboardButton(' 📋Termos de Uso', url='https://telegra.ph/Termos-de-Uso-07-15'))

    await bot.send_chat_action(chat_id=call.from_user.id, action='typing')
    await bot.answer_callback_query(callback_query_id=call.id)

    if chat_id in messages:
        await bot.edit_message_text(chat_id=chat_id, message_id=messages[chat_id], text=f"""Seja bem vindo! \n
Sou o <b>Vadox</b> 🧞‍♂️, seu assistente inteligente! 🤖

Por favor, selecione o departamento que melhor atende sua necessidade. 👇 """, reply_markup=markup)
    else:
        # Se a mensagem original não for encontrada, envia uma nova mensagem
        sent_message = await bot.send_message(chat_id, f"""Seja bem vindo! \n
Sou o <b>Vadox</b> 🧞‍♂️, seu assistente inteligente! 🤖

Por favor, selecione o departamento que melhor atende sua necessidade. 👇 """, reply_markup=markup)

        # Armazena o ID da nova mensagem
        messages[chat_id] = sent_message.message_id



@bot.callback_query_handler(func=lambda call: call.data == 'bot_explorer')
async def callback_bot_explorer(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
        InlineKeyboardButton('💻 Canais Diversos', callback_data='canais'),
        InlineKeyboardButton('◀️ Retornar', callback_data='start')
        )
    await bot.send_chat_action(chat_id=call.from_user.id, action='typing')
    await bot.edit_message_text('💻 Navegue pelos canais sugeridos', chat_id, message_id, reply_markup=markup)



@bot.callback_query_handler(func=lambda call: call.data == 'canais')
async def callback_canais(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    markup = InlineKeyboardMarkup()
    markup.row_width = 3
    markup.add(InlineKeyboardButton('🎵 Músicas', callback_data='musicas'),
                InlineKeyboardButton('📺 Filmes', callback_data='filmes'),
                InlineKeyboardButton('🗞 Notícias', callback_data='noticias'),
                InlineKeyboardButton('🌎 Mundo', callback_data='mundo'),
                # InlineKeyboardButton('🗿 RedPill', callback_data='redpill'),
                InlineKeyboardButton('💻 Tecnologia', callback_data='tecnologia'),
                InlineKeyboardButton('📚 Cursos', callback_data='cursos'),
                InlineKeyboardButton('🔡 Idiomas', callback_data='idiomas'),
                InlineKeyboardButton('🕹 Games', url='https://t.me/gamee')
                )
    markup.add(InlineKeyboardButton('◀️ Retornar', callback_data='bot_explorer'))
    await bot.send_chat_action(chat_id=call.from_user.id, action='typing')
    await bot.edit_message_text('💻 Canais', chat_id, message_id, reply_markup=markup)
    


@bot.callback_query_handler(func=lambda call: call.data == 'musicas')
async def callback_musicas(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    markup = InlineKeyboardMarkup()
    markup.row_width = 3
    markup.add(InlineKeyboardButton('🎤 Rap', callback_data='rap'),
                InlineKeyboardButton('🪘 Pagode', callback_data='pagode'),
                InlineKeyboardButton('🔊 Funk', callback_data='funk'),
                InlineKeyboardButton('🎸 Rock', callback_data='rock'),
                InlineKeyboardButton('🎹 Jazz', callback_data='jazz'),
                InlineKeyboardButton('🎷 Blues', callback_data='blues'))
    markup.add(InlineKeyboardButton('◀️ Retornar', callback_data='canais'))
    await bot.send_chat_action(chat_id=call.from_user.id, action='typing')
    await bot.edit_message_text('🎵 Músicas', chat_id, message_id, reply_markup=markup)



@bot.callback_query_handler(func=lambda call: call.data == 'rap')
async def callback_rap(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("🎤 Racionais Mc's", url='https://t.me/musicaracionaismcs'),
                InlineKeyboardButton('🎤 Rap Nacional', url='https://t.me/rapnacionaloriginal'),
                InlineKeyboardButton('🎤 Gospel Rap', url='https://t.me/Gospelrapmusic'),
                InlineKeyboardButton('🎤 G-Funk', url='https://t.me/gfunk_music'))
    markup.add(InlineKeyboardButton('◀️ Retornar', callback_data='musicas'))
    await bot.send_chat_action(chat_id=call.from_user.id, action='typing')
    await bot.edit_message_text('🎤 Rap', chat_id, message_id, reply_markup=markup)



@bot.callback_query_handler(func=lambda call: call.data == 'pagode')
async def callback_pagode(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("🪘  Pagode do Bom", url='https://t.me/Pagodes1600Misturados'))
    markup.add(InlineKeyboardButton('◀️ Retornar', callback_data='musicas'))
    await bot.send_chat_action(chat_id=call.from_user.id, action='typing')
    await bot.edit_message_text('🪘 Pagode', chat_id, message_id, reply_markup=markup)



@bot.callback_query_handler(func=lambda call: call.data == 'funk')
async def callback_funk(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("🔊 Fluxo do Funk", url='https://t.me/Aaaaabcrd'))
    markup.add(InlineKeyboardButton('◀️ Retornar', callback_data='musicas'))
    await bot.send_chat_action(chat_id=call.from_user.id, action='typing')
    await bot.edit_message_text('🔊 Funk', chat_id, message_id, reply_markup=markup)



@bot.callback_query_handler(func=lambda call: call.data == 'rock')
async def callback_rock(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("🎸 Rock Som das Antigas", url='https://t.me/somdasantigas'))
    markup.add(InlineKeyboardButton('◀️ Retornar', callback_data='musicas'))
    await bot.send_chat_action(chat_id=call.from_user.id, action='typing')
    await bot.edit_message_text('🎸 Rock', chat_id, message_id, reply_markup=markup)



@bot.callback_query_handler(func=lambda call: call.data == 'jazz')
async def callback_jazz(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("🎹 Jazz Music Relaxing", url='https://t.me/songjazz'))
    markup.add(InlineKeyboardButton('◀️ Retornar', callback_data='musicas'))
    await bot.send_chat_action(chat_id=call.from_user.id, action='typing')
    await bot.edit_message_text('🎹 Jazz', chat_id, message_id, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'blues')
async def callback_blues(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("🎷 Blues Music Relaxing", url='https://t.me/songblues'))
    markup.add(InlineKeyboardButton('◀️ Retornar', callback_data='musicas'))
    await bot.send_chat_action(chat_id=call.from_user.id, action='typing')
    await bot.edit_message_text('🎷 Blues', chat_id, message_id, reply_markup=markup)



@bot.callback_query_handler(func=lambda call: call.data == 'filmes')
async def callback_filmes(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton('📺 Filmes Arte', url='https://t.me/FilmsArte'),
                InlineKeyboardButton('📺 Testosterona', url='https://t.me/Testosteronaa'),
                InlineKeyboardButton('📺 TopFlix', url='https://t.me/TopFlixx_Bot'),
                InlineKeyboardButton('📺 Filmes Policiais', url='https://t.me/cineminhapolicial'),
                InlineKeyboardButton('📺 Filmes e Séries', url='https://t.me/filmes'),
                InlineKeyboardButton('📺 Filmes Atores', url='https://t.me/filmes_atores'))
    markup.add(InlineKeyboardButton('🔞 Adulto', callback_data='adulto'))
    markup.add(InlineKeyboardButton('◀️ Retornar', callback_data='canais'))
    await bot.send_chat_action(chat_id=call.from_user.id, action='typing')
    await bot.edit_message_text('📺 Filmes', chat_id, message_id, reply_markup=markup)



@bot.callback_query_handler(func=lambda call: call.data == 'adulto')
async def callback_adulto(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("🔞 Amadoras BR", url='https://t.me/amadorasbrcaiunaneteafins'),
                InlineKeyboardButton('🔞 Machismo Realista', url='https://t.me/MachismoRealistaAbsoluto'),
                InlineKeyboardButton('🔞 Wheyfus', url='https://t.me/wheyfus'),
                InlineKeyboardButton('🔞 Comedores de Preta', url='https://t.me/ComedordePreta'),
                InlineKeyboardButton('🔞 Revista +18', url='https://t.me/+4QqllZAPjYA0MDJh'),
                )
    markup.add(InlineKeyboardButton('◀️ Retornar', callback_data='filmes'))
    await bot.send_chat_action(chat_id=call.from_user.id, action='typing')
    await bot.edit_message_text('🔞 Adulto', chat_id, message_id, reply_markup=markup)



@bot.callback_query_handler(func=lambda call: call.data == 'noticias')
async def callback_noticias(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("🗞 Tupi Report", url='https://t.me/tupireport'),
                InlineKeyboardButton('🗞 InfoMoney', url='https://t.me/infomoney_noticias'))
    markup.add(InlineKeyboardButton('◀️ Retornar', callback_data='canais'))
    await bot.send_chat_action(chat_id=call.from_user.id, action='typing')
    await bot.edit_message_text('🗞 Notícias', chat_id, message_id, reply_markup=markup)



@bot.callback_query_handler(func=lambda call: call.data == 'mundo')
async def callback_mundo(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("🌎 Live Leak", url='https://t.me/leaklive'))
    markup.add(InlineKeyboardButton('◀️ Retornar', callback_data='canais'))
    await bot.send_chat_action(chat_id=call.from_user.id, action='typing')
    await bot.edit_message_text('🌎 Mundo', chat_id, message_id, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'tecnologia')
async def callback_tec(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("📱 Termux Hacker ", url='https://t.me/Termux_For_Android'))
    markup.add(InlineKeyboardButton("📱 Termux Hacking Commands ", url='https://t.me/Termux_Hacking_TLS'))
    markup.add(InlineKeyboardButton('◀️ Retornar', callback_data='canais'))
    await bot.send_chat_action(chat_id=call.from_user.id, action='typing')
    await bot.edit_message_text('💻 Tecnologia', chat_id, message_id, reply_markup=markup)



@bot.callback_query_handler(func=lambda call: call.data == 'cursos')
async def callback_cursos(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("📚 Learn Ethical Hacking", url='https://t.me/wh8teHatHacking'),
                InlineKeyboardButton('💻 DevWorld - Cursos', url='https://t.me/DevWorldSbot'))
    markup.add(InlineKeyboardButton('◀️ Retornar', callback_data='canais'))
    await bot.send_chat_action(chat_id=call.from_user.id, action='typing')
    await bot.edit_message_text('📚 Cursos', chat_id, message_id, reply_markup=markup)



@bot.callback_query_handler(func=lambda call: call.data == 'idiomas')
async def callback_idiomas(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton('🏴󠁧󠁢󠁥󠁮󠁧󠁿 Inglês 🏴󠁧󠁢󠁥󠁮󠁧󠁿', url='https://t.me/inglespelotelegram'),
                InlineKeyboardButton('🇪🇸 Espanhol 🇪🇸', url='https://t.me/espanholcombeta'),
                InlineKeyboardButton('🇫🇷 Francês 🇫🇷', url='https://t.me/francesmairovergara'),
                InlineKeyboardButton('🇩🇪 Alemão 🇩🇪', url='https://t.me/Cursoalemao'))
    markup.add(InlineKeyboardButton('◀️ Retornar', callback_data='canais'))
    await bot.send_chat_action(chat_id=call.from_user.id, action='typing')
    await bot.edit_message_text('🔡 Idiomas', chat_id, message_id, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'financeiro')
async def callback_financeiro(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id

    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('Recarregar Saldo', callback_data='recarregar_saldo')),
    markup.add(InlineKeyboardButton('Depósito Não Creditado', callback_data='deposito_nao_creditado')),
    markup.add(InlineKeyboardButton('Reembolsos e Estornos', callback_data='reembolso_e_estornos'))
    markup.add(InlineKeyboardButton('◀️ Retornar', callback_data='start'))
    await bot.send_chat_action(chat_id=call.from_user.id, action='typing')
    await bot.answer_callback_query(callback_query_id=call.id)
    await bot.edit_message_text(""" 🌟 Base de Conhecimento

Abaixo, muitas dúvidas relacionadas já foram respondidas! 💡 """,
chat_id, message_id, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'recarregar_saldo')
async def callback_recarregar_saldo(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('◀️ Retornar', callback_data='financeiro'))
    await bot.send_chat_action(chat_id=call.from_user.id, action='typing')
    await bot.edit_message_text("""
            Passo 1: Leia os Termos de Uso 📖
Antes de adicionar saldo, é crucial ler nossos termos para garantir uma convivência harmoniosa. Está tudo lá para o benefício mútuo!

Passo 2: Métodos de Pagamento 💳
Oferecemos métodos seguros via Mercado Pago, incluindo PIX, Saldo em Conta e PayPal.

Passo 3: Adicionando Saldo
Digite o comando /recarregar.

Passo 4: Informe os Detalhes 📝
Digite o valor desejado. Se for sua primeira vez, precisaremos do seu Nome/CPF para a emissão do documento fiscal. Fique tranquilo, seus dados estão seguros!

Passo 5: Concluindo o Pagamento ✔️
Você será redirecionado para o Mercado Pago para concluir sua transação. Escolha o método de pagamento de sua preferência.

Passo 6: Confirmação do Pagamento 🔄
O Mercado Pago nos notificará assim que o pagamento for aprovado. O PIX é instantâneo, mas qualquer atraso, por favor, nos avise ou contate seu banco.

Passo 7: Pronto! 🎉
Uma vez confirmado, enviaremos uma notificação via bot. Agora, você está pronto para aproveitar e gerar seus números virtuais!

            """, chat_id, message_id, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'deposito_nao_creditado')
async def callback_deposito_nao_creditado(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('◀️ Retornar', callback_data='financeiro'))
    await bot.send_chat_action(chat_id=call.from_user.id, action='typing')
    await bot.edit_message_text("""
            🔍 Pagamento Não Creditado na Conta?

Passo 1: Verifique a Forma de Pagamento 💳
Se o dinheiro não apareceu no saldo, vamos investigar. Certifique-se de especificar a forma de pagamento escolhida e envie o comprovante da transação com o arquivo anexado.

Passo 2: Possíveis Razões para o Atraso ⏳
Pode ser que o pagamento esteja pendente por motivos como:
- Informações Incorretas: Confira se os detalhes do pagamento estão corretos, incluindo nome e CPF.
- Limite de Crédito Insuficiente: Verifique se há limite suficiente para a compra.
- Transação Suspeita: O banco pode estar verificando se a transação é legítima.

Passo 3: Aguarde e Contate seu Banco 🏦
Aguardar alguns minutos é recomendado para o processamento. Se ainda estiver pendente, entre em contato com seu banco para verificar o status da transação. Eles podem fornecer informações sobre qualquer possível retenção do pagamento.

🕒 Tempo é a Chave
Às vezes, tudo o que é necessário é um pouco mais de tempo para o banco validar a transação. Mantenha a calma!

Se precisar de mais ajuda, estamos aqui para orientar você durante o processo. 🆘\n
            """, chat_id, message_id, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'reembolso_e_estornos')
async def reembolso_e_estornos(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('◀️ Retornar', callback_data='financeiro'))
    await bot.send_chat_action(chat_id=call.from_user.id, action='typing')
    await bot.edit_message_text("""
            🔄 Solicitação de Reembolso: Saiba Como Proceder

Para pedir reembolso, é simples, mas siga nossos termos de uso. O reembolso começa a contar 1 hora após a recarga em nossas plataformas.

⏰ Prazo Importante: 7 Dias Corridos

Você tem até 7 dias a partir da compra para solicitar reembolso, desde que o valor recarregado não tenha sido utilizado.

❗️Limitações e Considerações Importantes
• O reembolso é limitado ao valor recarregado.
• Saldo anterior e bonificações não entram no reembolso.
• A política segue o Código de Defesa do Consumidor e a Lei do E-commerce.

⚠️ Importante: ⚠️
O reembolso é válido apenas se o saldo não foi utilizado. Fique tranquilo, seguimos as leis para garantir transparência e justiça em todo o processo.

Para iniciar o processo de reembolso, certifique-se de atender a esses requisitos e entre em contato conosco. Estamos aqui para ajudar! 🌐✨\n
            """, chat_id, message_id, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'suporte_tecnico')
async def callback_suporte_tecnico(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('Reabastecimento', callback_data='reabastecimento')),
    markup.add(InlineKeyboardButton('Número Banido/Utilizado', callback_data='numero_banido_utilizado')),
    markup.add(InlineKeyboardButton('Recomendações', callback_data='recomendacoes'))
    markup.add(InlineKeyboardButton('SMS Não Recebido!', callback_data='sms_nao_recebido'))
    markup.add(InlineKeyboardButton('SMS Incorreto', callback_data='sms_incorreto'))
    markup.add(InlineKeyboardButton('◀️ Retornar', callback_data='start'))
    await bot.send_chat_action(chat_id=call.from_user.id, action='typing')
    await bot.edit_message_text(""" 🌟 Base de Conhecimento

Abaixo, muitas dúvidas relacionadas já foram respondidas! 💡 """,
chat_id, message_id, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'reabastecimento')
async def callback_reabastecimento(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('◀️ Retornar', callback_data='suporte_tecnico'))
    await bot.send_chat_action(chat_id=call.from_user.id, action='typing')
    await bot.edit_message_text("""
            🔢 Reabastecimento de Números

Recarga Regular: Sem Horários Definidos
Os números são reabastecidos regularmente, sem hora marcada. Quer ser um dos primeiros a conseguir? Clique em "Comprar" para entrar na fila e garantir os números recém-adicionados.

📲 Receba Alertas de Reabastecimento
Para obter alertas instantâneos sobre reabastecimentos, use o comando /alertas no bot.

🌍 Números Estrangeiros: Uma Opção Alternativa
Se os números que você precisa não estão disponíveis há um tempo, considere procurar em outros países. Temos uma lista completa de países e serviços disponíveis para você explorar.

🔒 Necessidade de Conexão Segura
Lembre-se, para usar números estrangeiros, é essencial estar conectado a um Proxy ou VPN para garantir a conexão correta.

Esta é uma maneira rápida de garantir os números que você deseja! Explore as opções e esteja preparado para aproveitar ao máximo nossos serviços. 🌐✨
            """, chat_id, message_id, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'numero_banido_utilizado')
async def callback_numero_banido_utilizado(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('◀️ Retornar', callback_data='suporte_tecnico'))
    await bot.send_chat_action(chat_id=call.from_user.id, action='typing')
    await bot.edit_message_text("""
            🚫 Problemas com Números: Entenda

Às vezes, você pode encontrar números já usados ou banidos. Isso ocorre quando a operadora reemite um número previamente cadastrado. Infelizmente, nenhum serviço de ativação online é imune a esses riscos, pois a verificação antecipada é tecnicamente desafiadora.

🔄 Reparação de Números: Requisitos Importantes

1️⃣ Banimento Prévio:
• Solicite estorno de saldo se o número foi banido antes da ativação.
• Apresente provas documentadas, como capturas de tela ou vídeos do registro.

2️⃣ Erro de Ativação:
• Não é possível solicitar estorno após a ativação, a menos que haja evidência documentada de banimento prévio.

3️⃣ Recurso com Prova:
• Siga os passos corretos e apresente provas documentadas para recorrer pelos canais de suporte.

4️⃣ Suporte sem Prova:
• O suporte sem comprovação documentada não resultará em reparação.
• É crucial seguir os requisitos para garantir uma avaliação adequada.

‼️ Importante:
• O estorno será concedido em saldo na plataforma, não em dinheiro.
• Pode ser usado para futuras aquisições em nosso serviço de números virtuais temporários.

Entendemos os desafios e estamos aqui para ajudar, desde que as evidências necessárias sejam fornecidas. 🛠️💬
            """, chat_id, message_id, reply_markup=markup)  


@bot.callback_query_handler(func=lambda call: call.data == 'recomendacoes')
async def callback_recomendacoes(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('◀️ Retornar', callback_data='suporte_tecnico'))
    await bot.send_chat_action(chat_id=call.from_user.id, action='typing')
    await bot.edit_message_text("""
🔸 Dicas Importantes para Usar Números Temporários

Alguns sites e apps têm segurança extra para evitar números temporários. Aqui vão algumas recomendações para evitar problemas:

• 🛡️ Use uma VPN.
• 🗑️ Limpe os dados do app.
• 🚫 Evite emuladores.
• 🌐 Navegue em guia anônima e limpe cache e cookies do navegador.
• ⚠️ Evite muitas tentativas no mesmo número, IP ou dispositivo.

🔸 Números Desativados: O Que Fazer?

Alguns números podem não funcionar, pois foram desativados pela operadora. Não se preocupe, você pode cancelar ou solicitar outro. Só cobramos do seu saldo quando você recebe o SMS.

🔸 Segurança é Prioridade

Mantenha seus cadastros seguros em apps e sites. Não somos responsáveis por perdas após o uso dos números.

🔸 Evite Cancelamentos Frequentes

Cancelar vários números pode levar a penalidades, como desconto de saldo e bloqueio. Siga as dicas acima para aproveitar ao máximo os números sem problemas.

Estas dicas vão te ajudar a usar nossos serviços sem complicações! 📱✨
            """, chat_id, message_id, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data == 'sms_nao_recebido')
async def callback_sms_nao_recebido(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('◀️ Retornar', callback_data='suporte_tecnico'))
    await bot.send_chat_action(chat_id=call.from_user.id, action='typing')
    await bot.edit_message_text("""
            Nesses casos, você pode cancelar uma ativação e comprar outro número. 🔄 Há vários motivos para uma falha na entrega de mensagens. 🚫📩

Muitos serviços são sensíveis ao seu endereço de rede, por isso é importante usar Proxy ou VPN 🌐 do número do país do qual você está comprando. 🛡️

Além disso, você pode tentar outro navegador ou dispositivo, porque essas alterações às vezes ajudam nossos usuários. 🔄📲 E não se esqueça de escolher diferentes operadoras móveis ao comprar números.  Assim, você trabalhará com diferentes fornecedores e provedores de cartões SIM. 📞

Lembramos que uma ativação é considerada paga, se você recebeu o código de ativação solicitado. ✅ Se o código de ativação não chegar, os valores serão automaticamente devolvidos ao seu saldo. 💰
            """, chat_id, message_id, reply_markup=markup)



@bot.callback_query_handler(func=lambda call: call.data == 'sms_incorreto')
async def callback_sms_incorreto(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('◀️ Retornar', callback_data='suporte_tecnico'))
    await bot.send_chat_action(chat_id=call.from_user.id, action='typing')
    await bot.edit_message_text("""
            📵 Problemas com SMS? Saiba o Que Fazer

A mensagem SMS está incorreta? Aqui está o que fazer:

🔍 Solicite o Reenvio Gratuito:
- Se a mensagem estiver incorreta, peça o reenvio gratuito do segundo SMS no mesmo número, dentro de 20 minutos.

⏰ Tempo de Ativação:
- A segunda mensagem chega dentro do tempo do número ativo (15 a 20 minutos). Clique em "Repetir" após receber o primeiro código SMS.

🤔 Ainda com Problemas?
- Entre em contato conosco, envie prints e vídeos com data, horário e código incorreto para análise.
- Iniciaremos a análise do seu caso para reparar o valor do serviço com problema.

Estamos aqui para ajudar a resolver qualquer contratempo com rapidez e eficiência! 🚀📱
            """, chat_id, message_id, reply_markup=markup)


if __name__ == '__main__':
    print('Bot running...')
    import asyncio
    asyncio.run(bot.infinity_polling(skip_pending=True))