// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT License.

const { InputHints } = require('botbuilder');
const { ComponentDialog, DialogTurnStatus, WaterfallDialog} = require('botbuilder-dialogs');

const WATERFALL_DIALOG = 'waterfallDialog';
/**
 * This base class watches for common phrases like "help" and "cancel" and takes action on them
 * BEFORE they reach the normal bot logic.
 */
class InitialDialog extends ComponentDialog {
    constructor(id) {
        super(id || 'initialDialog');
        
        
        this.addDialog(new WaterfallDialog(WATERFALL_DIALOG, [
            this.onContinueDialog.bind(this),
            this.interrupt.bind(this),
                   
        ]));
        this.initialDialogId = WATERFALL_DIALOG;
        
    }
    async onContinueDialog(innerDc) {
        const result = await this.interrupt(innerDc);
        if (result) {
            return result;
        }
        return await super.onContinueDialog(innerDc);
    }

    async interrupt(innerDc) {
        if (innerDc.context.activity.text) {
            const text = innerDc.context.activity.text.toLowerCase();

            switch (text) {
            case 'help':
            case '?': {
                const helpMessageText = 'Show help here';
                await innerDc.context.sendActivity(helpMessageText, helpMessageText, InputHints.ExpectingInput);
                return { status: DialogTurnStatus.waiting };
            }
            case 'cancel':
            case 'exit':
            case 'quit': {
                const cancelMessageText = 'Cancelling...';
                await innerDc.context.sendActivity(cancelMessageText, cancelMessageText, InputHints.IgnoringInput);
                return await innerDc.cancelAllDialogs();
            }
            case 'registrera värden': {
                const registerMessageText = 'Okej du vill registrera värden';
                await innerDc.context.sendActivity(registerMessageText, registerMessageText, InputHints.ExpectingInput);
                return { status: DialogTurnStatus.waiting };
            }
            case 'ändra inställningar': {
                const registerMessageText = 'Du vill ändra inställningar';
                await innerDc.context.sendActivity(registerMessageText, registerMessageText, InputHints.ExpectingInput);
                return { status: DialogTurnStatus.waiting };
            }
            case 'boka konsultation': {
                const registerMessageText = 'Okej du vill boka konsultation';
                await innerDc.context.sendActivity(registerMessageText, registerMessageText, InputHints.ExpectingInput);
                return { status: DialogTurnStatus.waiting };
            }
            case 'övriga frågor': {
                const registerMessageText = 'Vad vill du fråga?';
                await innerDc.context.sendActivity(registerMessageText, registerMessageText, InputHints.ExpectingInput);
                return { status: DialogTurnStatus.waiting };
            }
        }
    }
    }
}

module.exports.InitialDialog = InitialDialog;
