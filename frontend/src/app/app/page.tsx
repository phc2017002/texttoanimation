import { Navbar } from "@/components/landing/Navbar";
import { VideoGenerator } from "@/components/app/VideoGenerator";

export default function AppPage() {
    return (
        <div className="min-h-screen bg-slate-50">
            <Navbar />
            <div className="py-12">
                <VideoGenerator />
            </div>
        </div>
    );
}
