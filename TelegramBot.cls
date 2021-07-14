global class TelegramBot {
   
    public static void main() {
		List<String> answer = get_updates();
        string answerChat_id = answer[0];
        string answerText = answer[1];
        if (answerText == '/Start' ){
        	send_message(answerChat_id , 'Введите логин');
           }
    }
    
    public static List<String> get_updates () {
        Telegram_bot__mdt[] token = [SELECT TokenTelegram__c FROM Telegram_bot__mdt];
        Telegram_bot__mdt[] URL = [SELECT URLTelegram__c FROM Telegram_bot__mdt];
		
        Http http = new Http();
        HttpRequest req = new HttpRequest();
        req.setMethod('GET');
        req.setHeader('Content-Type','application/x-www-form-urlencoded');
        req.setEndpoint(URL[0].URLTelegram__c + token[0].TokenTelegram__c + '/getupdates');
        HTTPResponse response = http.send(req);
        List<String> messageFull = new List<String>();
        if (response.getStatusCode() == 200) {
        Map<String, Object> data = (Map<String, object>)JSON.deserializeUntyped(response.getBody());
            List<Map<String, Object>> result = new List<Map<String, Object>>();
        for (Object instance : (List<Object>)data.get('result'))
            result.add((Map<String, Object>)instance);    
        Map<String, Object> message = (Map<String, Object>) result[result.size() - 1].get('message'); 
        Map<String, Object> chat = (Map<String, Object>) message.get('chat'); 
            
        String chat_id = String.valueOf(chat.get('id'));
        String message_text = String.valueOf(message.get('text')); 
		messageFull.add(chat_id);
        messageFull.add(message_text);    
        }
        return messageFull;        
    }
    
    public static void send_message (String chat_id, String text) {
        Telegram_bot__mdt[] token = [SELECT TokenTelegram__c FROM Telegram_bot__mdt];
        Telegram_bot__mdt[] URL = [SELECT URLTelegram__c FROM Telegram_bot__mdt];
		
        Http http = new Http();
        HttpRequest req = new HttpRequest();
        req.setMethod('GET');
        req.setHeader('Content-Type','application/x-www-form-urlencoded');
        req.setEndpoint(URL[0].URLTelegram__c + token[0].TokenTelegram__c + '/sendmessage?chat_id='+ chat_id +'&text='+ text);
        HTTPResponse response = http.send(req);   
    }
}