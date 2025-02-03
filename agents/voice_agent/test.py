from wake_word import WakeWordDetector

detector = WakeWordDetector(keyword_path="models/wake_word.ppn")
detector.listen_for_wake_word()  # Say your custom wake word!