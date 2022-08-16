use vkapi::{LongpollEvent, types::longpoll::LongpollUpdate};
use futures::StreamExt;

const TOKEN: &str = "70c3c8f087f11c6b1c9ae4ea75e3ee8cf814f4e21a6a895e0b65b36e135ec188f39e083c7547cfbda0bbd";
const LONGPOLL: u32 = 209597192;

#[tokio::main]
async fn main() {
    let mut vk_api = vkapi::VK::new("5.103".to_string(), "ru".to_string());
    vk_api.set_access_token(TOKEN.to_string());

    let mut stream = vk_api.init_stream(LONGPOLL, 25).await;

    stream.set_prefix("<префикс бота>");
    stream.set_allowed_events(&[LongpollEvent::MessageNew]);

    let mut stream = stream.build_stream();

    while let Some(update) = stream.next().await {
        if let LongpollUpdate::MessageNew { message } = update {
            println!("id: {}", message.id);
            println!("date: {}", message.date);
            println!("peer id: {}", message.peer_id);
            println!("conversation message id: {}", message.conversation_message_id);
            println!("from id: {}", message.from_id);
            println!("text: {}", message.text);
            println!("attachments: {:?}", message.attachments);
            println!("reply_message: {:?}", message.reply_message);
        }
    }
}