import express from "express";
import cors from "cors";
import helmet from "helmet";
import fileRoutes from "./routes/file.routes";

const app = express();

app.use(helmet());
app.use(cors({
  origin: "http://localhost:3000"
}));

app.use(express.json());

app.use("/api/files", fileRoutes);

export default app;