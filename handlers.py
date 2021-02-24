from methods import choose_answer, choose_caule, choose_ideia, choose_joelho


def start(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = "Oi, eu sou o Wanderley! manda um /meajuda pra eu saber como te ajudar, meu nobre!")

def meajuda(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = "Fala meu consagrado! Por enquanto é isso que eu faço:\n\n/opiniao - Ta na dúvida se deve ou não seguir com a ideia errada? Eu te dou a resposta!\n/ideia - Lanço a braba.\n/caule - Por sua conta e risco.\n/joelho - Meu joelho esquerdo dói quando algo vai dar errado.")

def opiniao(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = choose_answer())

def ideia(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = choose_ideia())

def caule(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = choose_caule())

def joelho(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = choose_joelho())

def unknown(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = "Ta loco?. Lança o /meajuda e me usa direito.")