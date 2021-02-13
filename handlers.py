from methods import choose_answer


def start(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = "Oi, eu sou o Wanderley! manda um /meajuda pra eu saber como te ajudar, meu nobre!")

def meajuda(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = "Fala meu consagrado! Por enquanto é isso que eu faço:\n\n/opiniao - Ta na dúvida se deve ou não seguir com a ideia errada? Eu te dou a resposta!\n/ideia - Lanço a braba")

def opiniao(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = choose_answer())

def ideia(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = "Tô poucas ideia hj parceiro, foi mal.")

def unknown(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = "Num fode mano, não sou deus não. Lança o /meajuda e me usa direito.")