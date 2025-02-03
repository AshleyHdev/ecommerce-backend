from app.database import engine
from app.models import Base

# 刪除所有表
Base.metadata.drop_all(bind=engine)
print("✅ 所有資料表已刪除。")

# 重新建立所有表
Base.metadata.create_all(bind=engine)
print("✅ 資料表重新建立成功。")