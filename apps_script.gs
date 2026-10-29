// Recebe as respostas da página e grava uma linha por pessoa numa planilha do Google.
// Passo a passo no README ("Receber as respostas numa planilha").

var COLUNAS = [
  "recebido_em", "numero", "versao", "ativo_s", "motivo_fim", "alcancados", "vistos",
  "estimativa", "sentimento", "reconhecidos", "reais", "falsos_marcados", "iscas",
  "pausas", "pausa_media_ms", "lembranca_livre", "temas_reais", "temas_marcados"
];

function doPost(e) {
  var lock = LockService.getScriptLock();
  lock.waitLock(10000);
  try {
    var d = JSON.parse(e.postData.contents);
    var planilha = SpreadsheetApp.getActiveSpreadsheet();
    var aba = planilha.getSheetByName("respostas") || planilha.insertSheet("respostas");
    if (aba.getLastRow() === 0) aba.appendRow(COLUNAS);
    aba.appendRow([
      new Date(), d.n, d.cond, d.ativo_s, d.motivo, d.alcancados, d.vistos,
      d.estimativa, d.sentimento, d.reconhecidos, d.reais, d.falsos_marcados, d.iscas,
      d.pausas, d.pausa_media_ms, d.livre, d.temas_reais, d.temas_marcados
    ]);
    return ContentService.createTextOutput("ok");
  } finally {
    lock.releaseLock();
  }
}

// Só para conferir no navegador que a implantação está de pé.
function doGet() {
  return ContentService.createTextOutput("recebendo");
}
