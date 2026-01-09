from config.Config import Config
from config.RuntimeContext import RuntimeContext
from duel_module.RescueDuel import RescueDuel
from duel_module.SpecialEventDuel import SpecialEventDuel
from util import DuelUtils, EventUtils


class EventDispatcherService():

    def __init__(self, config: Config, runtime_context: RuntimeContext):
        self.runtime_context = runtime_context
        self.config = config
        self.specialEventDuel = SpecialEventDuel(config, runtime_context)
        self.rescueDuel = RescueDuel(config, runtime_context)

    def dispatchEvent(self):
        if self.runtime_context.special_event_file_name is None:
            print("没有活动事件文件名")
            return

        while self.runtime_context.special_event_file_name is not None:
            print("开始处理活动事件:" + self.runtime_context.special_event_file_name)
            # 特殊人物决斗事件
            if self.runtime_context.special_event_file_name.startswith("appear.") \
                or self.runtime_context.special_event_file_name.startswith("event"):
                # 先清理文件名
                self.runtime_context.special_event_file_name = None
                self.specialEventDuel.duel()
            # 救援活动
            elif self.runtime_context.special_event_file_name.startswith("go") \
                or self.runtime_context.special_event_file_name.startswith("appearing."):
                self.rescueDuel.duel()





