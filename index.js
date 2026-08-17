const { Telegraf, Markup } = require('telegraf');
require('dotenv').config();

const BOT_TOKEN = process.env.BOT_TOKEN;
const CHANNEL_LINK = process.env.CHANNEL_LINK || 'https://t.me/+aZyjCO1v0yoxNWQ1';
const ADMIN_ID = process.env.ADMIN_ID;

if (!BOT_TOKEN) {
  console.error('ERROR: BOT_TOKEN is missing. Set it in your environment variables.');
  process.exit(1);
}

const bot = new Telegraf(BOT_TOKEN);

let dailyAnalysis =
  "Mets à jour cette section avec une vraie statistique ou analyse du jour via la commande /setanalysis.";

const DISCLAIMER = "\n\n⚠️ Contenu informatif — les paris sportifs comportent des risques.";

bot.start((ctx) => {
  const name = ctx.from.first_name || '';
  ctx.reply(
    `👋 Salut ${name} !\nBienvenue chez Lucas Analyse 📊⚽️\n\nIci, tu retrouveras des analyses de matchs, des statistiques et des pronostics football basés sur 7 ans d'expérience.\n\nQue veux-tu faire ?`,
    Markup.inlineKeyboard([
      [Markup.button.callback('📈 Voir l\'analyse du jour', 'daily_analysis')],
      [Markup.button.callback('ℹ️ En savoir plus', 'about')],
      [Markup.button.url('👥 Rejoindre la communauté', CHANNEL_LINK)],
    ])
  );
});

bot.action('daily_analysis', (ctx) => {
  ctx.answerCbQuery();
  ctx.reply(`📈 Analyse du jour :\n\n${dailyAnalysis}${DISCLAIMER}`,
    Markup.inlineKeyboard([
      [Markup.button.url('👥 Rejoindre la communauté pour plus d\'analyses', CHANNEL_LINK)],
    ])
  );
});

bot.action('about', (ctx) => {
  ctx.answerCbQuery();
  ctx.reply(
    "Lucas Analyse propose des analyses football quotidiennes basées sur des statistiques réelles : forme des équipes, historique des confrontations, tendances de buts, etc.\n\n" +
    "7 ans d'expérience dans l'analyse sportive.\n" +
    "Communauté internationale." + DISCLAIMER,
    Markup.inlineKeyboard([
      [Markup.button.url('👥 Rejoindre la communauté', CHANNEL_LINK)],
    ])
  );
});

bot.command('setanalysis', (ctx) => {
  if (String(ctx.from.id) !== String(ADMIN_ID)) {
    return;
  }
  const text = ctx.message.text.replace('/setanalysis', '').trim();
  if (!text) {
    return ctx.reply('Utilisation : /setanalysis <ton texte ici>');
  }
  dailyAnalysis = text;
  ctx.reply('✅ Analyse du jour mise à jour.');
});

bot.on('text', (ctx) => {
  ctx.reply("Utilise /start pour voir le menu principal 📊");
});

bot.launch();
console.log('Bot démarré...');

process.once('SIGINT', () => bot.stop('SIGINT'));
process.once('SIGTERM', () => bot.stop('SIGTERM'));
