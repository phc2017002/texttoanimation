"use client";

import React, { useState, useEffect } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { Loader2, Upload, Link as LinkIcon, FileText, CheckCircle, AlertCircle, Download, Play, Layout, Clock, Settings } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Input, Textarea } from "@/components/ui/input";
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card";
import { api, type InputType, type Category, type JobStatus } from "@/lib/api";
import { cn } from "@/lib/utils";

export function VideoGenerator() {
  const [inputType, setInputType] = useState<InputType>("text");
  const [category, setCategory] = useState<Category>("tech_system");
  const [content, setContent] = useState("");
  const [isGenerating, setIsGenerating] = useState(false);
  const [currentJob, setCurrentJob] = useState<JobStatus | null>(null);
  const [error, setError] = useState<string | null>(null);

  // Poll for job status
  useEffect(() => {
    let interval: NodeJS.Timeout;

    if (currentJob && ["pending", "generating_code", "rendering"].includes(currentJob.status)) {
      interval = setInterval(async () => {
        try {
          const status = await api.getJobStatus(currentJob.job_id);
          setCurrentJob(status);

          if (status.status === "failed") {
            setError(status.error || "Job failed");
            setIsGenerating(false);
          } else if (status.status === "completed") {
            setIsGenerating(false);
          }
        } catch (e) {
          console.error("Polling error", e);
        }
      }, 2000);
    }

    return () => clearInterval(interval);
  }, [currentJob]);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!content) return;

    setIsGenerating(true);
    setError(null);
    setCurrentJob(null);

    try {
      const job = await api.createVideo(content, inputType, category);
      setCurrentJob({
        job_id: job.job_id,
        status: "pending",
        progress: { percentage: 0, message: "Starting..." },
        created_at: new Date().toISOString()
      });
    } catch (e: any) {
      setError(e.message);
      setIsGenerating(false);
    }
  };

  const categories: { value: Category; label: string }[] = [
    { value: "tech_system", label: "Tech & System Design" },
    { value: "product_startup", label: "Product & Startup" },
    { value: "mathematical", label: "Math & Research" },
  ];

  return (
    <div className="flex h-[calc(100vh-4rem)]">
      {/* Sidebar */}
      <div className="w-64 bg-slate-900 border-r border-slate-800 hidden md:flex flex-col p-4">
        <div className="space-y-2">
          <Button variant="ghost" className="w-full justify-start text-blue-400 bg-blue-500/10 hover:bg-blue-500/20 hover:text-blue-300">
            <Layout className="mr-2 h-4 w-4" />
            Dashboard
          </Button>
          <Button variant="ghost" className="w-full justify-start text-slate-400 hover:text-white hover:bg-slate-800">
            <Clock className="mr-2 h-4 w-4" />
            History
          </Button>
          <Button variant="ghost" className="w-full justify-start text-slate-400 hover:text-white hover:bg-slate-800">
            <Settings className="mr-2 h-4 w-4" />
            Settings
          </Button>
        </div>

        <div className="mt-auto pt-4 border-t border-slate-800">
          <div className="bg-slate-800/50 rounded-lg p-4">
            <div className="text-xs font-medium text-slate-400 uppercase mb-2">Usage</div>
            <div className="h-2 bg-slate-700 rounded-full overflow-hidden mb-2">
              <div className="h-full bg-blue-500 w-[30%]"></div>
            </div>
            <div className="text-xs text-slate-500">3/10 videos generated</div>
          </div>
        </div>
      </div>

      {/* Main Content */}
      <div className="flex-1 overflow-auto bg-slate-950 p-8">
        <div className="max-w-5xl mx-auto space-y-8">

          <div className="flex justify-between items-center">
            <div>
              <h1 className="text-2xl font-bold text-white">Create New Animation</h1>
              <p className="text-slate-400">Transform your ideas into precise visual explanations.</p>
            </div>
          </div>

          <div className="grid lg:grid-cols-3 gap-8">
            {/* Input Section */}
            <div className="lg:col-span-2 space-y-6">
              <Card className="bg-slate-900 border-slate-800">
                <CardContent className="p-6">
                  <form onSubmit={handleSubmit} className="space-y-6">
                    {/* Input Type Selection */}
                    <div className="grid grid-cols-3 gap-4">
                      <button
                        type="button"
                        onClick={() => setInputType("text")}
                        className={cn(
                          "flex flex-col items-center p-4 rounded-xl border transition-all",
                          inputType === "text"
                            ? "border-blue-500 bg-blue-500/10 text-blue-400"
                            : "border-slate-800 bg-slate-900 text-slate-400 hover:border-slate-700 hover:bg-slate-800"
                        )}
                      >
                        <FileText className="w-6 h-6 mb-2" />
                        <span className="font-medium text-sm">Text Prompt</span>
                      </button>
                      <button
                        type="button"
                        onClick={() => setInputType("url")}
                        className={cn(
                          "flex flex-col items-center p-4 rounded-xl border transition-all",
                          inputType === "url"
                            ? "border-blue-500 bg-blue-500/10 text-blue-400"
                            : "border-slate-800 bg-slate-900 text-slate-400 hover:border-slate-700 hover:bg-slate-800"
                        )}
                      >
                        <LinkIcon className="w-6 h-6 mb-2" />
                        <span className="font-medium text-sm">URL / Blog</span>
                      </button>
                      <button
                        type="button"
                        onClick={() => setInputType("pdf")}
                        className={cn(
                          "flex flex-col items-center p-4 rounded-xl border transition-all",
                          inputType === "pdf"
                            ? "border-blue-500 bg-blue-500/10 text-blue-400"
                            : "border-slate-800 bg-slate-900 text-slate-400 hover:border-slate-700 hover:bg-slate-800"
                        )}
                      >
                        <Upload className="w-6 h-6 mb-2" />
                        <span className="font-medium text-sm">PDF Paper</span>
                      </button>
                    </div>

                    {/* Category Selection */}
                    <div className="space-y-3">
                      <label className="text-sm font-medium text-slate-400">Animation Style</label>
                      <div className="grid grid-cols-3 gap-4">
                        {categories.map((cat) => (
                          <button
                            key={cat.value}
                            type="button"
                            onClick={() => setCategory(cat.value)}
                            className={cn(
                              "px-4 py-3 rounded-lg text-sm font-medium transition-all border",
                              category === cat.value
                                ? "bg-slate-800 text-white border-slate-700 ring-1 ring-blue-500/50"
                                : "bg-slate-900 text-slate-400 border-slate-800 hover:border-slate-700 hover:bg-slate-800"
                            )}
                          >
                            {cat.label}
                          </button>
                        ))}
                      </div>
                    </div>

                    {/* Content Input */}
                    <div className="space-y-3">
                      <label className="text-sm font-medium text-slate-400">
                        {inputType === "text" ? "Describe your animation" :
                          inputType === "url" ? "Paste the URL" : "Upload PDF File"}
                      </label>
                      {inputType === "text" ? (
                        <Textarea
                          placeholder="Explain the concept of neural networks using a simple analogy..."
                          className="min-h-[200px] text-base resize-none bg-slate-950 border-slate-800 text-slate-200 focus:border-blue-500 focus:ring-blue-500/20"
                          value={content}
                          onChange={(e) => setContent(e.target.value)}
                        />
                      ) : inputType === "url" ? (
                        <Input
                          placeholder="https://example.com/article"
                          value={content}
                          onChange={(e) => setContent(e.target.value)}
                          className="bg-slate-950 border-slate-800 text-slate-200"
                        />
                      ) : (
                        <div className="border-2 border-dashed border-slate-800 rounded-xl p-8 text-center hover:border-slate-700 hover:bg-slate-900/50 transition-colors">
                          <Input
                            type="file"
                            accept=".pdf"
                            onChange={async (e) => {
                              const file = e.target.files?.[0];
                              if (file) {
                                const reader = new FileReader();
                                reader.onload = (event) => {
                                  const base64 = event.target?.result as string;
                                  const base64Content = base64.split(',')[1];
                                  setContent(base64Content);
                                };
                                reader.readAsDataURL(file);
                              }
                            }}
                            className="hidden"
                            id="pdf-upload"
                          />
                          <label htmlFor="pdf-upload" className="cursor-pointer">
                            <Upload className="h-10 w-10 text-slate-500 mx-auto mb-4" />
                            <p className="text-sm text-slate-400 font-medium">Click to upload PDF</p>
                            <p className="text-xs text-slate-600 mt-1">Maximum file size 10MB</p>
                          </label>
                          {content && (
                            <div className="mt-4 flex items-center justify-center text-green-400 text-sm bg-green-400/10 py-2 px-4 rounded-full inline-flex">
                              <CheckCircle className="h-4 w-4 mr-2" />
                              PDF Loaded
                            </div>
                          )}
                        </div>
                      )}
                    </div>

                    <Button
                      type="submit"
                      size="lg"
                      className="w-full text-lg h-14 bg-blue-600 hover:bg-blue-500 text-white shadow-lg shadow-blue-500/25"
                      disabled={isGenerating || !content}
                    >
                      {isGenerating ? (
                        <>
                          <Loader2 className="mr-2 h-5 w-5 animate-spin" />
                          Processing...
                        </>
                      ) : (
                        <>
                          <Play className="mr-2 h-5 w-5" />
                          Generate Video
                        </>
                      )}
                    </Button>
                  </form>
                </CardContent>
              </Card>
            </div>

            {/* Status & Preview Section */}
            <div className="lg:col-span-1">
              <AnimatePresence mode="wait">
                {currentJob ? (
                  <motion.div
                    initial={{ opacity: 0, x: 20 }}
                    animate={{ opacity: 1, x: 0 }}
                    exit={{ opacity: 0, x: 20 }}
                    className="sticky top-8"
                  >
                    <Card className="bg-slate-900 border-slate-800 overflow-hidden">
                      <CardHeader className="border-b border-slate-800 bg-slate-900/50">
                        <CardTitle className="text-lg text-white flex items-center gap-2">
                          {currentJob.status === "completed" ? (
                            <CheckCircle className="h-5 w-5 text-green-400" />
                          ) : currentJob.status === "failed" ? (
                            <AlertCircle className="h-5 w-5 text-red-400" />
                          ) : (
                            <Loader2 className="h-5 w-5 text-blue-400 animate-spin" />
                          )}
                          {currentJob.status === "completed" ? "Ready to Download" : "Generating..."}
                        </CardTitle>
                      </CardHeader>
                      <CardContent className="p-6 space-y-6">
                        {/* Progress */}
                        {currentJob.status !== "completed" && currentJob.status !== "failed" && (
                          <div className="space-y-3">
                            <div className="flex justify-between text-sm">
                              <span className="text-slate-400">{currentJob.progress.message}</span>
                              <span className="text-blue-400 font-mono">{currentJob.progress.percentage}%</span>
                            </div>
                            <div className="h-2 bg-slate-800 rounded-full overflow-hidden">
                              <motion.div
                                className="h-full bg-blue-500"
                                initial={{ width: 0 }}
                                animate={{ width: `${currentJob.progress.percentage}%` }}
                                transition={{ duration: 0.5 }}
                              />
                            </div>
                          </div>
                        )}

                        {/* Video Player */}
                        {currentJob.status === "completed" && (
                          <div className="space-y-4">
                            <div className="aspect-video bg-slate-950 rounded-lg overflow-hidden border border-slate-800 relative group">
                              <video
                                src={api.getVideoUrl(currentJob.job_id)}
                                controls
                                className="w-full h-full"
                                poster="/placeholder-video.jpg"
                              />
                            </div>
                            <Button className="w-full bg-slate-800 hover:bg-slate-700 text-white" asChild>
                              <a href={api.getVideoUrl(currentJob.job_id)} download>
                                <Download className="mr-2 h-4 w-4" />
                                Download MP4
                              </a>
                            </Button>
                          </div>
                        )}

                        {/* Error Display */}
                        {error && (
                          <div className="p-4 bg-red-500/10 border border-red-500/20 text-red-400 rounded-lg text-sm">
                            {error}
                          </div>
                        )}

                        {/* Job Details */}
                        <div className="pt-4 border-t border-slate-800">
                          <div className="grid grid-cols-2 gap-4 text-xs text-slate-500">
                            <div>
                              <div className="uppercase tracking-wider mb-1">Job ID</div>
                              <div className="font-mono text-slate-400 truncate">{currentJob.job_id.slice(0, 8)}...</div>
                            </div>
                            <div>
                              <div className="uppercase tracking-wider mb-1">Quality</div>
                              <div className="text-slate-400">1080p60</div>
                            </div>
                          </div>
                        </div>
                      </CardContent>
                    </Card>
                  </motion.div>
                ) : (
                  <div className="h-full flex items-center justify-center border-2 border-dashed border-slate-800 rounded-xl p-8 text-slate-600">
                    <div className="text-center">
                      <div className="bg-slate-900 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
                        <Play className="h-8 w-8 text-slate-700" />
                      </div>
                      <p>Your generated video will appear here</p>
                    </div>
                  </div>
                )}
              </AnimatePresence>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
