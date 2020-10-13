const { ConfirmPrompt, TextPrompt, ComponentDialog, WaterfallDialog } = require('botbuilder-dialogs');


const CONFIRM_PROMPT = 'confirmPrompt';
const TEXT_PROMPT = 'textPrompt';
const WATERFALL_DIALOG = 'waterfallDialog';

class RegisterDialog extends ComponentDialog {
    constructor(id) {
        super(id || 'registerDialog');
        //console.log("i register dialog constructor");
        this.addDialog(new TextPrompt(TEXT_PROMPT))
            .addDialog(new ConfirmPrompt(CONFIRM_PROMPT))
            .addDialog(new WaterfallDialog(WATERFALL_DIALOG, [
                this.firstStep.bind(this)

            ]));

        this.registerDialogId = WATERFALL_DIALOG;
    }

    async firstStep(stepContext) {
        //const registerDetails = stepContext.options;

        const messageText = 'Vilket värde vill du registrera?';
        const msg = MessageFactory.text(messageText, messageText, InputHints.ExpectingInput);
        
        return await stepContext.prompt(TEXT_PROMPT, { prompt: msg });
     
        
    }
}

    module.exports.RegisterDialog = RegisterDialog;