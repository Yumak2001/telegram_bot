from aiogram.utils.executor import Executor

from app.misc import dp


runner = Executor(dp)


def setup(skip_updates: bool):

    from app.utils.executor import runner

    runner.skip_updates = skip_updates
    runner.start_polling(reset_webhook=True)
