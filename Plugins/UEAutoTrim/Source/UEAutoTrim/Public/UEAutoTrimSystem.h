// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "Subsystems/GameInstanceSubsystem.h"
#include "UEAutoTrimSystem.generated.h"

UCLASS()
class UEAUTOTRIM_API UUEAutoTrimSystem : public UGameInstanceSubsystem, public FTickableGameObject
{
	GENERATED_BODY()
public:
	UUEAutoTrimSystem();
	virtual TStatId GetStatId() const override;
	virtual ETickableTickType GetTickableTickType() const override;
	virtual void Tick(float DeltaTime) override;
	virtual void Initialize(FSubsystemCollectionBase& Collection) override;
	virtual void Deinitialize() override;

	UFUNCTION(BlueprintCallable)
	void Start(const FString& InTagName);

	UFUNCTION(BlueprintCallable)
	void End();

	UFUNCTION(BlueprintPure)
	bool IsBusy() const;

	UFUNCTION(BlueprintCallable)
	void SetTextOffset(const FVector2D& InOffset);

	UFUNCTION(BlueprintCallable)
	void SetTextColor(const FLinearColor& InColor);

	UFUNCTION(BlueprintCallable)
	void SetBackgroundColor(const FLinearColor& InColor);

	UFUNCTION(BlueprintCallable)
	void SetBoxSize(const FVector2D& InSize);

	UFUNCTION(BlueprintCallable)
	void SetBoxPosition(const FVector2D& InPosition);

private:
	void Draw(UCanvas* InCanvas, APlayerController* InPC);

	UPROPERTY()
	UFont* Font;

	enum class EMode
	{
		None,
		Start,
		End
	};

	FDelegateHandle DebugDrawHandle;
	float ElapsedTime = 0;
	FString TagName;
	FText DisplayText;
	EMode Mode = EMode::None;
	FLinearColor TextColor = FLinearColor::White;
	FLinearColor BackgroundColor = FLinearColor::Black;
	FVector2D BoxSize = FVector2D(400, 20);
	FVector2D BoxPosition = FVector2D(0.0f, 0.0f);
	FVector2D TextOffset = FVector2D(10.0f, 2.0f);

	static TAutoConsoleVariable<float> CVarTagDisplayTime;
};
