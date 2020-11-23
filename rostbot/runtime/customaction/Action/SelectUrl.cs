using System;
using System.Runtime.CompilerServices;
using System.Threading;
using System.Threading.Tasks;
using AdaptiveExpressions.Properties;
using Microsoft.Bot.Builder.Dialogs;
using Newtonsoft.Json;
using System.Net;
using System.Net.NetworkInformation;

namespace Microsoft.BotFramework.Composer.CustomAction
{
    /// <summary>
    /// Custom command which takes takes 2 data bound arguments (arg1 and arg2) and multiplies them returning that as a databound result.
    /// </summary>
    public class SelectUrl : Dialog
    {
        [JsonConstructor]
        public SelectUrl([CallerFilePath] string sourceFilePath = "", [CallerLineNumber] int sourceLineNumber = 0)
            : base()
        {
            // enable instances of this command as debug break point
            this.RegisterSourceLocation(sourceFilePath, sourceLineNumber);
        }

        [JsonProperty("$kind")]
        public const string Kind = "SelectUrl";

        /// <summary>
        /// Gets or sets memory path to bind to arg1 (ex: conversation.width).
        /// </summary>
        /// <value>
        /// Memory path to bind to arg1 (ex: conversation.width).
        /// </value>
        [JsonProperty("arg1")]
        public StringExpression Arg1 { get; set; }

        /// <summary>
        /// Gets or sets memory path to bind to arg2 (ex: conversation.height).
        /// </summary>
        /// <value>
        /// Memory path to bind to arg2 (ex: conversation.height).
        /// </value>
        [JsonProperty("arg2")]
        public StringExpression Arg2 { get; set; }

        /// <summary>
        /// Gets or sets caller's memory path to store the result of this step in (ex: conversation.area).
        /// </summary>
        /// <value>
        /// Caller's memory path to store the result of this step in (ex: conversation.area).
        /// </value>
        [JsonProperty("resultProperty")]
        public StringExpression ResultProperty { get; set; }


        private bool validHost(Uri uri, Ping ping) {
            Console.WriteLine("Sending ping to "+ uri + " with uri " + uri.Host + "...");
            var res = ping.Send(uri.Host);
            Console.WriteLine("Sent ping to " + uri +", received " + res);
            return res.Status == IPStatus.Success;
        }

        public override Task<DialogTurnResult> BeginDialogAsync(DialogContext dc, object options = null, CancellationToken cancellationToken = default(CancellationToken))
        {

            var arg1 = Arg1.GetValue(dc.State);
            var arg2 = Arg2.GetValue(dc.State);

            var ping = new Ping();
            Uri uri = new Uri(arg1);

            String result;

            if(validHost(new Uri(arg1), ping)) {
                result = arg1;
            }
            else if(validHost(new Uri(arg2), ping)) {
                result = arg2;
            }
            else {
                result = "host_not_found";
                Console.WriteLine(result);
            }

            // Convert.ToInt32(arg1) * Convert.ToInt32(arg2);
            if (this.ResultProperty != null)
            {
                dc.State.SetValue(this.ResultProperty.GetValue(dc.State), result);
            }

            return dc.EndDialogAsync(result: result, cancellationToken: cancellationToken);
        }

        
    }
}
