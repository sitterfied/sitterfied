//Luhn algorithm identifier verification
//MIT Licensed
function isValidIdentifier(identifier) {

    var sum     = 0,
        alt     = false,
        i       = identifier.length-1,
        num;

    if (identifier.length < 13 || identifier.length > 19){
        return false;
    }

    while (i >= 0){

        //get the next digit
        num = parseInt(identifier.charAt(i), 10);

        //if it's not a valid number, abort
        if (isNaN(num)){
            return false;
        }

        //if it's an alternate number...
        if (alt) {
            num *= 2;
            if (num > 9){
                num = (num % 10) + 1;
            }
        } 

        //flip the alternate bit
        alt = !alt;

        //add to the rest of the sum
        sum += num;

        //go to next digit
        i--;
    }

    //determine if it's valid
    return (sum % 10 == 0);
}

function getCreditCardType(accountNumber) {

  //start without knowing the credit card type
  var result = "unknown";

  //first check for MasterCard
  if (/^5[1-5]/.test(accountNumber))
  {
    result = "mastercard";
  }

  //then check for Visa
  else if (/^4/.test(accountNumber))
  {
    result = "visa";
  }

  //then check for AmEx
  else if (/^3[47]/.test(accountNumber))
  {
    result = "amex";
  }
  
  else if (/^6(?:011|5)/.test(accountNumber)) {
    result = "discover"
  }

  return result;
}

function handleCreditCardIndetification(event) {
    var value = event.target.value;
    setCreditCardLogo(value);
}

function setCreditCardLogo(value) {
    var type = getCreditCardType(value);
    switch(type) {
        case "mastercard":
            $(".credit-card-logo").html('<img id="creditcard-image" src="/static/images/icons/mastercard.png" />');
            break;
        case "visa":
            $(".credit-card-logo").html('<img id="creditcard-image" src="/static/images/icons/visa.png" />');
            break;
        case "amex":
            $(".credit-card-logo").html('<img id="creditcard-image" src="/static/images/icons/americanexpress.png" />');
            break;
        case "discover":
            $(".credit-card-logo").html('<img id="creditcard-image" src="/static/images/icons/discover.png" />');
            break;

        default:
            $(".credit-card-logo").html("");
    }
}